-- Render ```mermaid blocks to PNG with mermaid-cli, so they show as diagrams
-- instead of source. Falls back to the source block if mmdc fails.
local function render(text)
  local base = os.tmpname()
  local mmd, png = base .. '.mmd', base .. '.png'
  local f = assert(io.open(mmd, 'w'))
  f:write(text)
  f:close()
  local ok, err = pcall(
    pandoc.pipe,
    os.getenv('MERMAID_BIN') or 'mmdc',
    { '-i', mmd, '-o', png, '--size', '1600', '-b', 'white', '-s', '2', '-q' },
    ''
  )
  os.remove(mmd)
  if not ok then
    io.stderr:write('mermaid.lua: mmdc failed, leaving source: ' .. tostring(err) .. '\n')
    return nil
  end
  return png
end

function CodeBlock(el)
  if not el.classes:includes('mermaid') then return nil end
  local png = render(el.text)
  if not png then return nil end
  local img = pandoc.Image({}, png)
  img.attributes.width = '80%'
  return pandoc.Para({ img })
end
