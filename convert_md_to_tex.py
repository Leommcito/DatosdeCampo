#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
convert_md_to_tex.py
Convierte Metodologia_final_corregido.md a Metodologia_final_corregido.tex
Procesamiento secuencial linea por linea.
Motor objetivo: xelatex (UTF-8 nativo)
"""

import re
import sys

INPUT_FILE = "Metodologia_final_corregido.md"
OUTPUT_FILE = "Metodologia_final_corregido.tex"

# ---------------------------------------------------------------------------
# Utilidades de escape
# ---------------------------------------------------------------------------

def escape_latex(text, in_table=False, in_url=False, in_verbatim=False):
    """
    Escapa caracteres especiales de LaTeX.
    - No escapa $ si parece estar en modo matematico (ya envuelto en $...$)
    - No escapa & dentro de entornos tabular
    - No escapa _ dentro de URLs
    - No escapa { } si ya son parte de un comando LaTeX (heuristica simple)
    """
    if in_verbatim:
        return text

    result = text

    # ~ -> \textasciitilde{}
    result = result.replace('~', r'\textasciitilde{}')
    # ^ -> \textasciicircum{}
    result = result.replace('^', r'\textasciicircum{}')

    # % -> \%
    result = result.replace('%', r'\%')

    # # -> \#
    result = result.replace('#', r'\#')

    if not in_table:
        # & -> \& (fuera de tablas)
        result = result.replace('&', r'\&')

    if not in_url:
        # _ -> \_
        result = result.replace('_', r'\_')

    # $ -> \$  (heuristica: si no esta ya entre $...$)
    result = result.replace('$', r'\$')
    # Desescapar modos matematicos simples: \$...\$ -> $...$
    result = re.sub(r'\\\$([^\\\$]+)\\\$', r'$\1$', result)

    # { y } -> \{ \}  (heuristica: si no parecen parte de comando \cmd{...})
    result = _unescape_braces(result)

    return result


def escape_latex_simple(text):
    """Escape minimo para texto que NO tiene comandos LaTeX."""
    result = text
    result = result.replace('~', r'\textasciitilde{}')
    result = result.replace('^', r'\textasciicircum{}')
    result = result.replace('%', r'\%')
    result = result.replace('#', r'\#')
    result = result.replace('&', r'\&')
    result = result.replace('_', r'\_')
    result = result.replace('$', r'\$')
    result = _unescape_braces(result)
    return result


# ---------------------------------------------------------------------------
# Procesamiento inline
# ---------------------------------------------------------------------------

def process_inline_formatting(text, in_table=False):
    """Aplica formato inline: bold, italic, code, links, emojis, footnote refs."""
    # Notas al pie: [^N] -> \footnote{...} (se resuelven despues)
    # Por ahora dejamos un marcador

    # Links: [texto](url) -> \href{url}{texto}
    # Preservar URLs con caracteres especiales
    def link_repl(m):
        link_text = m.group(1)
        url = m.group(2)
        # Escapar caracteres especiales en el texto del link
        link_text = escape_latex_simple(link_text)
        return r'\href{' + url + '}{' + link_text + '}'
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link_repl, text)

    # Bold: **text** -> \textbf{text}
    # Usamos un loop para manejar anidamiento simple
    while True:
        new_text = re.sub(r'\*\*([^*]+)\*\*', r'\\textbf{\1}', text)
        if new_text == text:
            break
        text = new_text

    # Italic: *text* -> \textit{text}
    # Cuidado: no reemplazar los * de listas (ya procesadas) ni los ** ya reemplazados
    # Como procesamos inline despues de estructura, los * de lista ya no estan aqui.
    while True:
        new_text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'\\textit{\1}', text)
        if new_text == text:
            break
        text = new_text

    # Code inline: `code` -> \texttt{code}
    text = re.sub(r'`([^`]+)`', r'\\texttt{\1}', text)

    # Emojis
    text = text.replace('✅', r'\checkmark{}')
    text = text.replace('❌', r'\xmark{}')
    text = text.replace('🔒', r'\lock{}')

    # Escapar caracteres especiales LaTeX restantes
    text = escape_latex(text, in_table=in_table)

    return text


def _unescape_braces(text):
    r"""Desescapa \{ y \} que son parte de comandos LaTeX conocidos."""
    result = text.replace('{', r'\{').replace('}', r'\}')
    result = re.sub(r'\\([a-zA-Z]+)\\\{', r'\\\1{', result)
    result = re.sub(r'\\\}', r'}', result)
    return result


def process_inline_for_table_cell(text, footnotes=None):
    """Procesa formato inline dentro de celdas de tabla."""
    # Notas al pie
    if footnotes:
        def fn_repl(m):
            num = m.group(1)
            if num in footnotes:
                content = footnotes[num]
                content_processed = process_inline_formatting(content)
                return r'\footnote{' + content_processed + '}'
            return r'\footnote{Nota ' + num + '}'
        text = re.sub(r'\[\^(\d+)\]', fn_repl, text)

    # Bold e italic dentro de celdas
    while True:
        new_text = re.sub(r'\*\*([^*]+)\*\*', r'\\textbf{\1}', text)
        if new_text == text:
            break
        text = new_text

    while True:
        new_text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'\\textit{\1}', text)
        if new_text == text:
            break
        text = new_text

    text = re.sub(r'`([^`]+)`', r'\\texttt{\1}', text)

    # Emojis
    text = text.replace('✅', r'\checkmark{}')
    text = text.replace('❌', r'\xmark{}')
    text = text.replace('🔒', r'\lock{}')

    # Escapar caracteres especiales, pero NO & (separador de columna) ni \ (fin de fila)
    text = text.replace('~', r'\textasciitilde{}')
    text = text.replace('^', r'\textasciicircum{}')
    text = text.replace('%', r'\%')
    text = text.replace('#', r'\#')
    text = text.replace('_', r'\_')
    text = text.replace('$', r'\$')
    text = _unescape_braces(text)

    return text


# ---------------------------------------------------------------------------
# Detectores de linea
# ---------------------------------------------------------------------------

def is_header(line):
    m = re.match(r'^(#{1,6})\s+(.*)$', line)
    if m:
        level = len(m.group(1))
        title = m.group(2).strip()
        return level, title
    return None, None


def is_table_line(line):
    return '|' in line


def is_table_separator(line):
    # Linea como |---|---| o |:--|:--| etc.
    stripped = line.strip()
    if not stripped.startswith('|'):
        return False
    # Remover primer y ultimo | si existen
    content = stripped[1:]
    if content.endswith('|'):
        content = content[:-1]
    parts = [p.strip() for p in content.split('|')]
    # Si todos los parts son solo -, :, =
    for p in parts:
        if p and not re.match(r'^[:\-=]+$', p):
            return False
    return True


def is_list_item(line):
    m = re.match(r'^(\s*)[-*]\s+(.*)$', line)
    if m:
        return len(m.group(1)), m.group(2)
    m = re.match(r'^(\s*)\d+\.\s+(.*)$', line)
    if m:
        return len(m.group(1)), m.group(2), True  # ordered
    return None


def is_blockquote(line):
    m = re.match(r'^>\s?(.*)$', line)
    if m:
        return m.group(1)
    return None


def is_horizontal_rule(line):
    stripped = line.strip()
    return stripped == '---' or stripped == '***' or stripped == '___'


def is_code_fence(line):
    stripped = line.strip()
    if stripped.startswith('```'):
        lang = stripped[3:].strip()
        return True, lang
    return False, None


# ---------------------------------------------------------------------------
# Conversor principal
# ---------------------------------------------------------------------------

def convert_md_to_tex(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = [l.lstrip('\ufeff') for l in f.readlines()]

    # Fase 0: Extraer definiciones de notas al pie
    footnotes = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r'^\[\^(\d+)\]:\s*(.*)$', line.strip())
        if m:
            num = m.group(1)
            content = m.group(2)
            # Puede haber continuacion en lineas siguientes (indentadas o no vacias)
            j = i + 1
            while j < len(lines):
                next_line = lines[j]
                if next_line.strip() == '':
                    break
                # Si la siguiente linea es otra definicion o header, etc., parar
                if re.match(r'^\[\^\d+\]:', next_line.strip()):
                    break
                if next_line.strip().startswith('#'):
                    break
                if next_line.strip().startswith('|'):
                    break
                if next_line.strip().startswith('- ') or next_line.strip().startswith('* '):
                    break
                if re.match(r'^\s*\d+\.', next_line.strip()):
                    break
                content += ' ' + next_line.strip()
                j += 1
            footnotes[num] = content
            i = j
        else:
            i += 1

    # Fase 1: Procesamiento secuencial
    out_lines = []
    out_lines.append(r'\input{latex-preamble}')
    out_lines.append('')

    in_code_block = False
    code_buffer = []
    code_lang = ''

    in_table = False
    table_buffer = []
    table_aligns = []

    in_list = False
    list_stack = []  # pila de (indent, ordered)
    list_buffer = []

    in_blockquote = False
    bq_buffer = []

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Saltear lineas de definicion de nota al pie (ya procesadas)
        if re.match(r'^\[\^(\d+)\]:', stripped):
            i += 1
            continue

        # ---------------------------------------------------------------
        # Bloques de codigo
        # ---------------------------------------------------------------
        fence, lang = is_code_fence(line)
        if fence:
            if not in_code_block:
                in_code_block = True
                code_lang = lang
                code_buffer = []
            else:
                in_code_block = False
                out_lines.append(r'\begin{verbatim}')
                out_lines.extend([l.rstrip('\n') for l in code_buffer])
                out_lines.append(r'\end{verbatim}')
                out_lines.append('')
            i += 1
            continue

        if in_code_block:
            code_buffer.append(line)
            i += 1
            continue

        # ---------------------------------------------------------------
        # Tablas
        # ---------------------------------------------------------------
        if is_table_line(line):
            if not in_table:
                in_table = True
                table_buffer = []
                table_aligns = []
            # Detectar si es separador
            if is_table_separator(line):
                # Extraer alineaciones
                content = stripped[1:]
                if content.endswith('|'):
                    content = content[:-1]
                parts = [p.strip() for p in content.split('|')]
                aligns = []
                for p in parts:
                    if p.startswith(':') and p.endswith(':'):
                        aligns.append('c')
                    elif p.endswith(':'):
                        aligns.append('r')
                    elif p.startswith(':'):
                        aligns.append('l')
                    else:
                        aligns.append('l')
                table_aligns = aligns
                i += 1
                continue
            else:
                table_buffer.append(line)
                i += 1
                continue
        else:
            if in_table:
                # Cerrar tabla
                out_lines.append('')
                # Generar entorno tabular
                if table_aligns:
                    align_str = ''.join(table_aligns)
                else:
                    # Inferir numero de columnas de la primera fila
                    first = table_buffer[0].strip()
                    content = first[1:]
                    if content.endswith('|'):
                        content = content[:-1]
                    cols = len(content.split('|'))
                    align_str = 'l' * cols
                out_lines.append(r'\begin{tabular}{' + align_str + '}')
                out_lines.append(r'\hline')
                first_row = True
                for row_line in table_buffer:
                    row_stripped = row_line.strip()
                    content = row_stripped[1:]
                    if content.endswith('|'):
                        content = content[:-1]
                    cells = [c.strip() for c in content.split('|')]
                    processed_cells = []
                    for cell in cells:
                        if not cell:
                            processed_cells.append('')
                        else:
                            processed_cells.append(process_inline_for_table_cell(cell, footnotes=footnotes))
                    out_lines.append(' & '.join(processed_cells) + r' \\')
                    if first_row:
                        out_lines.append(r'\hline')
                        first_row = False
                out_lines.append(r'\hline')
                out_lines.append(r'\end{tabular}')
                out_lines.append('')
                in_table = False
                table_buffer = []
                table_aligns = []
            # No incrementar i aqui; procesar la linea actual normalmente

        # ---------------------------------------------------------------
        # Listas
        # ---------------------------------------------------------------
        list_info = is_list_item(line)
        if list_info:
            indent = list_info[0]
            item_text = list_info[1]
            ordered = list_info[2] if len(list_info) > 2 else False

            if not in_list:
                in_list = True
                list_stack = []
                list_buffer = []

            # Determinar nivel actual
            current_indent = list_stack[-1][0] if list_stack else -1

            if indent > current_indent:
                # Abrir nuevo nivel
                list_stack.append((indent, ordered))
                env = 'enumerate' if ordered else 'itemize'
                list_buffer.append((indent, ordered, r'\begin{' + env + '}'))
            elif indent < current_indent:
                # Cerrar niveles hasta encontrar el apropiado
                while list_stack and list_stack[-1][0] > indent:
                    last_indent, last_ordered = list_stack.pop()
                    env = 'enumerate' if last_ordered else 'itemize'
                    list_buffer.append((last_indent, last_ordered, r'\end{' + env + '}'))
                # Si no hay stack o el indent no coincide exactamente, abrir nuevo
                if not list_stack or list_stack[-1][0] != indent:
                    list_stack.append((indent, ordered))
                    env = 'enumerate' if ordered else 'itemize'
                    list_buffer.append((indent, ordered, r'\begin{' + env + '}'))
            else:
                # Mismo nivel, verificar si cambia tipo
                if list_stack and list_stack[-1][1] != ordered:
                    # Cerrar anterior y abrir nuevo tipo
                    last_indent, last_ordered = list_stack.pop()
                    env = 'enumerate' if last_ordered else 'itemize'
                    list_buffer.append((last_indent, last_ordered, r'\end{' + env + '}'))
                    list_stack.append((indent, ordered))
                    env = 'enumerate' if ordered else 'itemize'
                    list_buffer.append((indent, ordered, r'\begin{' + env + '}'))

            # Agregar item
            item_processed = process_inline_formatting(item_text)
            list_buffer.append((indent, ordered, r'\item ' + item_processed))
            i += 1
            continue
        else:
            if in_list:
                # Si la linea esta vacia o es solo espacios, puede ser fin de lista
                # O si la siguiente linea no es lista
                if stripped == '':
                    # Cerrar todas las listas
                    while list_stack:
                        last_indent, last_ordered = list_stack.pop()
                        env = 'enumerate' if last_ordered else 'itemize'
                        list_buffer.append((last_indent, last_ordered, r'\end{' + env + '}'))
                    # Volcar buffer
                    for _, _, cmd in list_buffer:
                        out_lines.append(cmd)
                    out_lines.append('')
                    in_list = False
                    list_stack = []
                    list_buffer = []
                    i += 1
                    continue
                else:
                    # Linea de continuacion de item (indentada o no)
                    # Agregar como texto adicional al ultimo item
                    # Simplemente agregamos como parrafo dentro del item
                    cont_text = process_inline_formatting(stripped)
                    # Reemplazar el ultimo item agregando un salto
                    if list_buffer:
                        last_indent, last_ordered, last_cmd = list_buffer[-1]
                        if last_cmd.startswith(r'\item '):
                            list_buffer[-1] = (last_indent, last_ordered, last_cmd + ' ' + cont_text)
                    i += 1
                    continue

        # ---------------------------------------------------------------
        # Blockquotes
        # ---------------------------------------------------------------
        bq_text = is_blockquote(line)
        if bq_text is not None:
            if not in_blockquote:
                in_blockquote = True
                bq_buffer = []
            bq_buffer.append(bq_text)
            i += 1
            continue
        else:
            if in_blockquote:
                out_lines.append(r'\begin{quote}')
                out_lines.append(process_inline_formatting(' '.join(bq_buffer)))
                out_lines.append(r'\end{quote}')
                out_lines.append('')
                in_blockquote = False
                bq_buffer = []
            # No incrementar i; procesar linea actual

        # ---------------------------------------------------------------
        # Reglas horizontales
        # ---------------------------------------------------------------
        if is_horizontal_rule(line):
            out_lines.append(r'\hline')
            out_lines.append('')
            i += 1
            continue

        # ---------------------------------------------------------------
        # Headers
        # ---------------------------------------------------------------
        level, title = is_header(line)
        if level:
            title_processed = process_inline_formatting(title)
            if level == 1:
                out_lines.append(r'\section{' + title_processed + '}')
            elif level == 2:
                out_lines.append(r'\subsection{' + title_processed + '}')
            elif level == 3:
                out_lines.append(r'\subsubsection{' + title_processed + '}')
            elif level == 4:
                out_lines.append(r'\paragraph{' + title_processed + '}')
            else:
                out_lines.append(r'\subparagraph{' + title_processed + '}')
            out_lines.append('')
            i += 1
            continue

        # ---------------------------------------------------------------
        # Linea en blanco
        # ---------------------------------------------------------------
        if stripped == '':
            out_lines.append('')
            i += 1
            continue

        # ---------------------------------------------------------------
        # Parrafo normal
        # ---------------------------------------------------------------
        # Reemplazar referencias de notas al pie [^N] -> \footnote{contenido}
        def footnote_repl(m):
            num = m.group(1)
            if num in footnotes:
                content = footnotes[num]
                content_processed = process_inline_formatting(content)
                return r'\footnote{' + content_processed + '}'
            else:
                return r'\footnote{Nota ' + num + '}'

        processed = re.sub(r'\[\^(\d+)\]', footnote_repl, stripped)
        processed = process_inline_formatting(processed)
        out_lines.append(processed)
        out_lines.append('')
        i += 1

    # Cierre de estados abiertos al final
    if in_code_block:
        out_lines.append(r'\begin{verbatim}')
        out_lines.extend([l.rstrip('\n') for l in code_buffer])
        out_lines.append(r'\end{verbatim}')
        out_lines.append('')

    if in_table:
        out_lines.append('')
        if table_aligns:
            align_str = ''.join(table_aligns)
        else:
            first = table_buffer[0].strip()
            content = first[1:]
            if content.endswith('|'):
                content = content[:-1]
            cols = len(content.split('|'))
            align_str = 'l' * cols
        out_lines.append(r'\begin{tabular}{' + align_str + '}')
        out_lines.append(r'\hline')
        first_row = True
        for row_line in table_buffer:
            row_stripped = row_line.strip()
            content = row_stripped[1:]
            if content.endswith('|'):
                content = content[:-1]
            cells = [c.strip() for c in content.split('|')]
            processed_cells = []
            for cell in cells:
                if not cell:
                    processed_cells.append('')
                else:
                        processed_cells.append(process_inline_for_table_cell(cell, footnotes=footnotes))
            out_lines.append(' & '.join(processed_cells) + r' \\')
            if first_row:
                out_lines.append(r'\hline')
                first_row = False
        out_lines.append(r'\hline')
        out_lines.append(r'\end{tabular}')
        out_lines.append('')

    if in_list:
        while list_stack:
            last_indent, last_ordered = list_stack.pop()
            env = 'enumerate' if last_ordered else 'itemize'
            list_buffer.append((last_indent, last_ordered, r'\end{' + env + '}'))
        for _, _, cmd in list_buffer:
            out_lines.append(cmd)
        out_lines.append('')

    if in_blockquote:
        out_lines.append(r'\begin{quote}')
        out_lines.append(process_inline_formatting(' '.join(bq_buffer)))
        out_lines.append(r'\end{quote}')
        out_lines.append('')

    # Escribir salida
    with open(output_path, 'w', encoding='utf-8') as f:
        for line in out_lines:
            f.write(line + '\n')

    print(f"Conversion completada: {output_path}")
    print(f"Total lineas procesadas: {len(lines)}")
    print(f"Notas al pie encontradas: {len(footnotes)}")


if __name__ == '__main__':
    convert_md_to_tex(INPUT_FILE, OUTPUT_FILE)
