'''
Данная функция реализует проверку заданного числа по указанной маске. Может оказаться довольно полезной для альтернативного решения задач 25 номера.
'''

def CheckNumber(number, mask):
    num_index = 0
    mask_index = 0
    while num_index < len(number) and mask_index < len(mask):
        if mask[mask_index] == '*':
            if mask_index == len(mask) - 1:
                return True
            while num_index < len(number) and number[num_index] != mask[mask_index+1]:
                num_index += 1
            mask_index += 1
        elif mask[mask_index] == '?':
            num_index += 1
            mask_index += 1
        else:
            if number[num_index] != mask[mask_index]:
                return False
            num_index += 1
            mask_index += 1
    return num_index == len(number) and mask_index == len(mask)
