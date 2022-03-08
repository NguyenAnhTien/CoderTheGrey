def find_score(num_cards, cards):
    left = 0
    right = num_cards - 1
    turn = 0
    sereja = 0
    dima = 0
    while left <= right:
        if cards[left] > cards[right]:
            if turn == 0:
                sereja += cards[left]
                turn = 1
            else:
                dima += cards[left]
                turn = 0
            left += 1
        else:
            if turn == 0:
               sereja += cards[right]
               turn = 1
            else:
               dima += cards[right]
               turn = 0
            right -= 1
    return sereja, dima

if __name__ == '__main__':
    num_cards = int(input())
    cards = list(map(int, input().split()))
    result = find_score(num_cards, cards)
    print(result[0], result[1])
