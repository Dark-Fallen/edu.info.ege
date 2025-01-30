"""
(ЕГКР-2024) Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может: 
– добавить в кучу 3 камня;
– добавить в кучу 6 камней;
– увеличить количество камней в куче в 3 раза. Например, из кучи в 20 камней за один ход можно получить кучу из 23, 26 или 60 камней. Игра завершается, когда количество камней в куче становится не менее 132. Победителем считается игрок, сделавший последний ход, то есть первым получивший кучу, в которой будет 132 или больше камней. В начальный момент в куче было S камней, 1 ≤ S ≤ 131. Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.
Задание 19. 
Укажите минимальное значение S, при котором Петя не может выиграть за один ход, но при любом ходе Пети Ваня может выиграть своим первым ходом.
Задание 20.
Найдите два наименьших значения S, когда Петя имеет выигрышную стратегию, причём одновременно выполняются два условия:
– Петя не может выиграть за один ход;
– Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
Найденные значения запишите в ответе в порядке возрастания.
Задание 21
Найдите минимальное значение S, при котором одновременно выполняются два условия:
– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.  

Ответ: №19: 41, №20: {14, 35}, №21: 32.
"""
def Game(state: int, step: int, goal: int, winner: int, min_step: int = 1, max_step: int = 2):
    if step > max_step: return False
    if state < goal:
        if step % 2 != winner:
            return any([Game(state + 3, step + 1, goal, winner, min_step, max_step),
                        Game(state + 6, step + 1, goal, winner, min_step, max_step),
                        Game(state * 3, step + 1, goal, winner, min_step, max_step)])
        return all([Game(state + 3, step + 1, goal, winner, min_step, max_step),
                        Game(state + 6, step + 1, goal, winner, min_step, max_step),
                        Game(state * 3, step + 1, goal, winner, min_step, max_step)])
    else:
        return winner == step % 2 and min_step <= step

print("№19:")   
# 19
for i in range(1, 132):
    if (Game(i, 0, 132, 0)):
        print(i)
        break

print("№20:") 
# 20
c = 0
for i in range(1, 131):
    if Game(i, 0, 132, 1, 2, 3):
        c += 1
        print(i)
    if c == 2:
        break

print("№21:") 
# 21
for i in range(1, 131):
    if Game(i, 0, 132, 0, 2, 4):
        print(i)
        break
