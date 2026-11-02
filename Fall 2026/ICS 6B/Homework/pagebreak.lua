local first_h1 = true
function Header(el)
  if el.level == 1 then
    if not first_h1 then
      return { pandoc.RawBlock('latex', '\\newpage'), el }
    end
    first_h1 = false
  end
end
