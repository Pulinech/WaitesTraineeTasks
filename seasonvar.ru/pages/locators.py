from selene.support.shared.jquery_style import s, ss
from selene import by, be, have
from selene import command
from selene import query


class SearchPageLocators:
    select_country = s("//select[@data-filter='country']/option[position()=3]")
    select_genre = s("//select[@data-filter='genre']/option[position()=3]")
    serials_links_side = ss("//div[@class='lside-serial']//a")
    serials_links_search = ss("//div[@class='news_n']/../..")
    country = s("//span[@itemprop='genre']/..//span[last()]")
    genre = s("//span[@itemprop='genre']")
    serials_names = ss("//div[@class='pgs-search-info']/a[position()=1]")
    original_name = s("//div[@class='pgs-sinfo_list']/span")
    alternative_name = s("//div[@class='pgs-sinfo_list']/span[last()]")
    start_player_btn = s("//pjsdiv[@id='oframehtmlPlayer']/pjsdiv[6]/pjsdiv[4]")
