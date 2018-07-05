#!/usr/bin/python

import os
import calendar

managed_endpoints = { 
    "lbnl#lrc":                "b2e0c23d-6d04-11e5-ba46-22000b92c6ec",
    "ucb#brc":                 "d47068d3-6d04-11e5-ba46-22000b92c6ec",
    "bearstore":               "3e3352d0-115e-11e6-a749-22000bf2d559",
    "lbnl#aresn-dtn":          "b23ee2c6-6d04-11e5-ba46-22000b92c6ec",
    "lbnl@aress-dtn":          "b23ee2dc-6d04-11e5-ba46-22000b92c6ec",
    "lbnl#cgrlvector":         "bafbb649-6d04-11e5-ba46-22000b92c6ec",
    "lbnl#cosmic-dtn":         "d922419a-4c97-11e8-8fd6-0a6d4e044368",
    "LBNL Gdrive Access":      "d0774b60-2549-11e7-bc62-22000b9a448b",
    "lbnl#irdata":             "9674ec8a-6920-11e8-9294-0a6d4e044368",
    "lbnl#metal":              "595ae84c-494f-11e6-8222-22000b97daec",
    "lbnl#oak":                "e4c16f48-6d04-11e5-ba46-22000b92c6ec",
    "lbnl#ares":               "dd1ee755-6d04-11e5-ba46-22000b92c6ec",
    "lbnl#mys3endpoint":       "eb412970-9210-11e5-9982-22000b96db58"
}

title = "title"
h1 = "h1"
h2 = "h2"
h3 = "h3"
h4 = "h4"
h5 = "h5"
h6 = "h6"
p = "p"

def doctype():
    return "<!doctype HTML>\n"

def start_html():
    return "<html>\n"

def end_html():
    return "</html>\n"

def start_head():
    return "<head>\n"

def end_head():
    return "</head>\n"

def start_body():
    return "<body>\n"

def end_body():
    return "</body>\n"

def tag(t, c, n=0):
    return "<" + t + ">" + c + "</" + t + ">" + ("\n" * n)

def hyperlink(h, c):
    return "<a href=\"" + h + "\">" + c + "</a>"

def br(n=1):
    return "<br />" * n

def ln(n=1):
    return "\n" * n

def hr():
    return "<hr />\n"

def brln(n=1):
    return "<br />" + ("\n" * n)

def hrln(n=1):
    return "<hr />" + ("\n" * n)

def start_table():
    return "<table>\n"

def end_table():
    return "</table>\n"

def start_row():
    return "<tr>\n"

def end_row():
    return "</tr>\n"

def header_cell(content):
    return "<th>" + content + "</th>\n"

def table_cell(content):
    return "<td>" + content + "</td>\n"

def main():
    paths = {}
    for k in managed_endpoints.keys():
        dk = k.replace('#', '_').replace('@', '_').replace(' ', '-')
        wdir = "www/" + dk
        if not os.path.exists(wdir):
            os.makedirs(wdir)
        sdir = "cache/" + managed_endpoints[k]
        ssubdirs = []
        if os.path.exists(sdir):
            ssubdirs = [name for name in os.listdir(sdir) if os.path.isdir(os.path.join(sdir, name))]
        #print(ssubdirs)
        for ssubdir in ssubdirs:
            sfiles = os.listdir(sdir + "/"  + ssubdir)
            for sfile in sfiles:
                paths[wdir + "/" + ssubdir + "_" + sfile] = (k, ssubdir, sfile)
    
    overwrite = 1
    for k in paths.keys():
        print(k + ": " + str(paths[k]))
        if not os.path.exists(k) or overwrite:
            summarize_month(k, paths[k][0], paths[k][1], paths[k][2])

def summarize_month(filename, endpoint, year, month):
    buf = ""

    buf += doctype()
    buf += start_html()
    buf += start_head()
    buf += tag(title, "Endpoint Usage Report", 1)
    buf += end_head()
    buf += start_body()

    buf += hyperlink("..", "<-- main menu")
    buf += brln()
    buf += hyperlink("../" + endpoint.replace('#', '_').replace('@', '_').replace(' ', '-'), "<-- " + endpoint + " menu")
    buf += brln()
    summary = calendar.month_name[int(month)] + " " + year + " monthly summary for Globus endpoint \"" + endpoint + "\" (" + managed_endpoints[endpoint] + "):"
    buf += tag(h2, summary)
    buf += ln(2)
    buf += hrln(2)

    buf += tag(h3, "Overall usage:")
    buf += ln(2)
    buf += start_table()
    buf += start_row()
    buf += header_cell("Tasks")
    buf += header_cell("Bytes")
    buf += header_cell("Files")
    buf += end_row()
    buf += start_row()
    buf += table_cell("FOO")
    buf += table_cell("BAR")
    buf += table_cell("BAZ")
    buf += end_row()
    buf += end_table()

    buf += end_body()
    buf += end_html()

    with open(filename, 'w') as fp:
        fp.seek(0)
        fp.write(buf)

if __name__ == "__main__":
    main()
