def black_box(page: int):
    if page <= 7922400:
        return True
    else:
        return False

def main():
    """
    Вам дали книгу, конкретное количество страниц вам не сообщили,
    но оно точно не превышает 10 000 000.
    
    Вам необходимо вычислить номер последней страницы.
    Книгу открывать нельзя - вместо этого вам выдали черный ящик, чтобы слегка усложнить задачу.
    Черному ящику (функция black_box) можно сообщить предполагаемый номер последней страницы,
    а в ответ узнать, есть ли эта страница в книге.
    
    Уточнение:
        black_box возвращает True, если страница последняя
                  возвращает False, если страница не последняя.
    
    
    Важно: написать наиболее эффективный алгоритм (по числу итераций)
    """
    # тут явно нужен алгоритм

    max_page = 10000000
    min_page = 0
    step = 0

    for i in range(max_page):

        step += 1
        mid = int((min_page + max_page) / 2)

        if black_box(mid) and black_box(mid - 1) and not (black_box(mid + 1)):
            print('amount page= ', mid, 'amount iterations= ', step)
            break

        if black_box(mid) and black_box(mid - 1) and (black_box(mid - 1)):
            min_page = mid + 1
        else:
            max_page = mid - 1



if __name__ == '__main__':
    main()

