def format_duration(sec):
    if sec == 0:
        return 'now'
    else:
        time = [0, 0, 0, 0, 0]
        time[4] = sec % 60
        time[3] = int(sec / 60) % 60
        time[2] = int(int(sec / 60) / 60) % 24
        time[1] = int(int(int(sec / 60) / 60) / 24) % 365
        time[0] = int(int(int(int(sec / 60) / 60) / 24) / 365)
        answ = ''
        cnt = 0
        cnt_amount = 0
        for i in range(0, 5):
            if time[i] > 0:
                cnt_amount += 1
        for i in range(0, 5):
            if time[i] > 0:
                cnt += 1
                in_between = (' and ' if cnt == cnt_amount - 1 else (', ' if cnt < cnt_amount - 1 else ''))
                if i == 0:
                    if time[i] == 1:
                        answ += str(time[i]) + ' year' + in_between
                    else:
                        answ += str(time[i]) + ' years' + in_between
                if i == 1:
                    if time[i] == 1:
                        answ += str(time[i]) + ' day' + in_between
                    else:
                        answ += str(time[i]) + ' days' + in_between
                if i == 2:
                    if time[i] == 1:
                        answ += str(time[i]) + ' hour' + in_between
                    else:
                        answ += str(time[i]) + ' hours' + in_between
                if i == 3:
                    if time[i] == 1:
                        answ += str(time[i]) + ' minute' + in_between
                    else:
                        answ += str(time[i]) + ' minutes' + in_between
                if i == 4:
                    if time[i] == 1:
                        answ += str(time[i]) + ' second'
                    else:
                        answ += str(time[i]) + ' seconds'

        return answ
