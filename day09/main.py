auction={}
def bid():
    name=input('enter your name:')
    auction[name]=int(input('enter your bid:'))
    ask=input('are there more bidders? yes or no\n')
    if ask=='yes':
        bid()
    else:
        winner={'winner':'','bid':0}
        for i in auction:
            if auction[i]>winner['bid']:
                winner['bid']=auction[i]
                winner['winner']=i
        print(f'The winner of auction is {winner["winner"]} with bid of {winner["bid"]}')
bid()
