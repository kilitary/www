import re

with open(r'/p/www/mq5_api.md', 'r', encoding='utf-8') as f:
    content = f.read()

functions = [
    'initialize', 'shutdown', 'version', 'last_error', 'account_info',
    'terminal_info', 'symbols_total', 'symbols_get', 'symbol_info',
    'symbol_info_tick', 'symbol_select', 'market_book_add', 'market_book_get',
    'market_book_release', 'copy_rates_from', 'copy_rates_from_pos',
    'copy_rates_range', 'copy_ticks_from', 'copy_ticks_range',
    'orders_total', 'orders_get', 'order_calc_margin', 'order_calc_profit',
    'order_check', 'order_send', 'positions_total', 'positions_get',
    'history_orders_total', 'history_orders_get', 'history_deals_total',
    'history_deals_get'
]

# Build index
index_lines = ['<a id="top"></a>', '', '## Index', '']
for func in functions:
    index_lines.append(f'- [{func}](#{func})')
index_lines.extend(['', '---', ''])

index_block = '\n'.join(index_lines)

# Insert index after first line (title)
lines = content.split('\n')
new_lines = [lines[0], index_block] + lines[1:]

# Add goto top links after each function heading
result = []
for line in new_lines:
    result.append(line)
    for func in functions:
        if line.strip() == f'## {func}':
            result.append('')
            result.append('[Back to top](#top)')
            result.append('')
            break

with open(r'/p/www/mq5_api.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(result))

print('Done! Added index and goto-top links.')
