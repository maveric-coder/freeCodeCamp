
def add_time(start, duration,day='zz'):
    days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    h1, m1 = map(int, start[:-2].split(':'))
    w=start[-2:]
    xx=duration.split(':')
    h2=int(xx[0])
    dd=0
    if h2>23:
        dd=h2//24
        h2%=24

    m2=int(xx[1])
    mm=m1+m2
    
    mf=0
    if mm>=60:
        mm-=60
        mf=1
        
    hh=h1+h2
    if mf==1:
        hh+=1
    f=0
    
    if hh>=24:
        hh-=12
        f=1
    if hh>11 and h1!=hh:
        f=1
    if hh>12:
        hh-=12
    
    if f==1:
        if w=='PM':
            w='AM'
            dd+=1
        else:
            w='PM'
        
    if dd>0:
        f=1
    hh=str(hh)
    mm=str(mm)
    
    ms=''
    if len(mm)==1:
        ms='0'
        ms+=mm
        mm=ms
    day=day.capitalize()
    if day!='Zz':
        xx=days.index(day)
    
    
    c=dd
    if f==1 and w=='AM' and day!='Zz':
        

        
        while dd>0:
            if xx==6:
                xx=0
            else:
                xx+=1
            dd-=1

    
    t=''
    if c==1:
        t='(next day)'
    elif c>1:
        t='('+str(c)+' days later)'
    
    if day!='Zz':
        nd=hh+':'+mm+' '+ w+', ' +days[xx]
        
    else:
        nd=hh+':'+mm+' '+w
        
    if c>0:
        if day!='Zz':
            nd=hh+':'+mm+' '+ w+', ' +days[xx]+' '+t
        
        else:
            nd=hh+':'+mm+' '+w+' '+t

    

    return nd