tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:                        
            crawled.append(page)
            for x in get_all_links(get_page(page)):
                tocrawl.append(x)
    return crawled