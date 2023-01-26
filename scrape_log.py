# most of the logs that we are reading are from where we are the challenger
# change PLAYER variable to "B" if we're reading a log where we were challenged
PLAYER = "A"

total_showdown_wins = 0
showdown_wins_awards = 0

total_showdown_losses = 0
showdown_losses_awards = 0

total_fold_wins = 0
fold_wins_awards = 0

total_fold_losses = 0
fold_losses_awards = 0


def read_file(filename):
    with open(filename) as inp:
        rounds = inp.read().split("Round #")
        inp.close()

    for i in range(len(rounds)):
        rounds[i] = rounds[i].splitlines()[1:-1]

    wins_showdown = {'number': 0, 'awarded': []}
    losses_showdown = {'number': 0, 'awarded': []}

    wins_fold = {'number': 0, 'awarded': []}
    losses_fold = {'number': 0, 'awarded': []}

    for _round in rounds:
        reached_showdown = False
        reached_fold = False
        amount_awarded = {}
        for action in _round:
            if "shows" in action:
                reached_showdown = True
            if "awarded" in action:
                player, awarded, amount = action.split(" ")
                amount_awarded[player] = int(amount)
            if "folds" in action:
                reached_fold = True
        
        if reached_showdown:
            if amount_awarded[PLAYER] >= 0:
                wins_showdown['number'] += 1
                wins_showdown['awarded'].append(amount_awarded[PLAYER])
            else:
                losses_showdown['number'] += 1
                losses_showdown['awarded'].append(amount_awarded[PLAYER])

        
        elif reached_fold: 
            if amount_awarded[PLAYER] >= 0:
                wins_fold['number'] += 1
                wins_fold['awarded'].append(amount_awarded[PLAYER])
            else:
                losses_fold['number'] += 1
                losses_fold['awarded'].append(amount_awarded[PLAYER])

    return wins_showdown, losses_showdown, wins_fold, losses_fold

for i in range(19):
    name = f"game_logs/game_log ({i}).txt"
    ws, ls, wf, lf = read_file(name)
    total_showdown_wins += ws['number']
    showdown_wins_awards += sum(ws['awarded'])

    total_showdown_losses += ls['number']
    showdown_losses_awards += sum(ls['awarded'])

    total_fold_wins += wf['number']
    fold_wins_awards += sum(wf['awarded'])

    total_fold_losses += lf['number']
    fold_losses_awards += sum(lf['awarded'])

try:
    ws_avg = showdown_wins_awards / total_showdown_wins
except(ZeroDivisionError):
    ws_avg = "N/A"
try:
    ls_avg = showdown_losses_awards / total_showdown_losses
except(ZeroDivisionError):
    ls_avg = "N/A"
try:
    wf_avg = fold_wins_awards / total_fold_wins
except(ZeroDivisionError):
    wf_avg = "N/A"
try:
    lf_avg = fold_losses_awards / total_fold_losses
except(ZeroDivisionError):
    lf_avg = "N/A"

print(f"Wins (Showdown): {total_showdown_wins}, Average Awarded: {ws_avg}")
print(f"Losses (Showdown): {total_showdown_losses}, Average Awarded: {ls_avg}")
print(f"Wins (Fold): {total_fold_wins}, Average Awarded: {wf_avg}")
print(f"Losses (Fold): {total_fold_losses}, Average Awarded: {lf_avg}")
