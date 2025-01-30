"""
Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежат две кучи камней. Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в одну из куч (по своему выбору) один камень, добавить три камня или увеличить количество камней в куче в два раза. Для того чтобы делать ходы, у каждого игрока есть неограниченное количество камней.
Игра завершается в тот момент, когда суммарное количество камней в кучах становится не менее 174. Победителем считается игрок, сделавший последний ход, т.е. первым получивший такую позицию, при которой в кучах оказывается 174 или больше камней. В начальный момент в первой куче было 19 камней, во второй куче – S камней; 1 ≤ S ≤ 154.
Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.
Задание 19. 
Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети. Укажите минимальное значение S, при котором такая ситуация возможна.
Задание 20.
Найдите два наименьших значения S, когда Петя имеет выигрышную стратегию, причём одновременно выполняются два условия:
– Петя не может выиграть за один ход;
– Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
Найденные значения запишите в ответе в порядке возрастания.
Задание 21
Найдите минимальное значение S, при котором одновременно выполняются два условия:
– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.  


Ответ: №19: 39
       №20: 74, 76
       №21: 75
"""

def Game(state: list[int], step: int, goal: int, winner: int, min_step: int = 1, max_step: int = 2, NoAI: bool = False):
    if step > max_step: return False
    if state[0] + state[1] < goal:
        if step % 2 != winner:
            return any([Game([state[0] + 1, state[1]], step + 1, goal, winner, min_step, max_step, NoAI),
                        Game([state[0] + 3, state[1]], step + 1, goal, winner, min_step, max_step, NoAI),
                        Game([state[0] * 2, state[1]], step + 1, goal, winner, min_step, max_step, NoAI),
                        Game([state[0], state[1] + 1], step + 1, goal, winner, min_step, max_step, NoAI),
                        Game([state[0], state[1] + 3], step + 1, goal, winner, min_step, max_step, NoAI),
                        Game([state[0], state[1] * 2], step + 1, goal, winner, min_step, max_step, NoAI)])
        return all([Game([state[0] + 1, state[1]], step + 1, goal, winner, min_step, max_step, NoAI),
                        Game([state[0] + 3, state[1]], step + 1, goal, winner, min_step, max_step, NoAI),
                        Game([state[0] * 2, state[1]], step + 1, goal, winner, min_step, max_step, NoAI),
                        Game([state[0], state[1] + 1], step + 1, goal, winner, min_step, max_step, NoAI),
                        Game([state[0], state[1] + 3], step + 1, goal, winner, min_step, max_step, NoAI),
                        Game([state[0], state[1] * 2], step + 1, goal, winner, min_step, max_step, NoAI)]) if not(NoAI) else any([Game([state[0] + 1, state[1]], step + 1, goal, winner, min_step, max_step, NoAI),
                        Game([state[0] + 3, state[1]], step + 1, goal, winner, min_step, max_step, NoAI),
                        Game([state[0] * 2, state[1]], step + 1, goal, winner, min_step, max_step, NoAI),
                        Game([state[0], state[1] + 1], step + 1, goal, winner, min_step, max_step, NoAI),
                        Game([state[0], state[1] + 3], step + 1, goal, winner, min_step, max_step, NoAI),
                        Game([state[0], state[1] * 2], step + 1, goal, winner, min_step, max_step, NoAI)]) 
    else:
        return winner == step % 2 and min_step <= step

#19 
print("№19: ", end='')
for i in range(1, 155):
    if Game([19, i], 0, 174, 0, 1, 2, True):
        print(i)
        break

#20
print("№20: ", end="")
c = 0
for i in range(1, 155):
    if Game([19, i], 0, 174, 1, 1, 3):
        if c < 1:
            print(i, end=", ")
        else: print(i)
        c += 1
    if c == 2:
        break

#21
print("№21: ", end="")
for i in range(1, 155):
    if Game([19, i], 0, 174, 0, 2, 4):
        print(i)
        break
