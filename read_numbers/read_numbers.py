def read_numbers(li):
    """연속된 숫자 배열을 받아서 연속된 숫자를 문자열로 변환한다.

    Args:
        li (list): 정렬된 상태의 숫자 배열 (ex. [1, 3, 4, 5, 10])

    Returns:
        string: 연속된 숫자를 변환한 문자열 (ex. "1, 3~5, 10")

    """
    result = ''
    s_list = []
    idx = 0

    while idx < len(li):
        if not s_list:
            s_list.append(str(li[idx]))
            s_list.append('')
            idx += 1

        # 연속된 숫자인 경우
        elif li[idx] == li[idx - 1] + 1:
            s_list[1] = str(li[idx])
            idx += 1

        # 연속된 숫자가 아닌 경우
        elif li[idx] != li[idx - 1] + 1:
            if s_list[1]:
                result += '~'.join(s_list)
            else:
                result += s_list[0]
            result += ', '
            s_list.clear()

    if s_list[1]:
        result += '~'.join(s_list)
    else:
        result += s_list[0]

    return result
