'''Shorter encoding for CodeClash in Python
from the solution to https://www.codingame.com/clashofcode/clash/report/2722974f6344c1e5bbee389efd1f40ce7c9be5f

Makes the program prg shorter IF len(prg)>= 52
'''

prg = '''c=gets
r=''
(97..c.ord).each{r=r+_1.chr+r}
puts r'''

if len(prg) % 2:
    prg += '\n'
# print(len(prg))
prg_enc = ''
for i in range(0, len(prg), 2):
    l, h = ord(prg[i]), ord(prg[i + 1])
    prg_enc += chr(256 * h + l)
res = f'exec(bytes("{prg_enc}","U16")[2:])'
# exec(bytes(prg_enc,"U16")[2:])
print(res)
print(len(res), 'vs', len(prg), 'characters!')
# G=lambda:map(int,input().split());G();print(sum(a**b for a,b in zip(G(),G())))

# exec(bytes("㵇慬扭慤洺灡椨瑮椬灮瑵⤨献汰瑩⤨਩⡇਩牰湩⡴畳⡭⩡截映牯愠戬椠⁮楺⡰⡇Ⱙ⡇⤩⤩","U16")[2:])
# equivalent to
#     exec('G=lambda:map(int,input().split())\nG()\nprint(sum(a**b for a,b in zip(G(),G())))')

# from the solution to https://www.codingame.com/clashofcode/clash/report/2722974f6344c1e5bbee389efd1f40ce7c9be5f
# ttt = bytes("㵇慬扭慤洺灡椨瑮椬灮瑵⤨献汰瑩⤨਩⡇਩牰湩⡴畳⡭⩡截映牯愠戬椠⁮楺⡰⡇Ⱙ⡇⤩⤩","U16")
# p(ttt)
# p(len(ttt))
# p(len(bytes("㵇慬扭慤洺灡椨瑮椬灮瑵⤨献汰瑩⤨਩⡇਩牰湩⡴畳⡭⩡截映牯愠戬椠⁮楺⡰⡇Ⱙ⡇⤩⤩","U16")))
# p(len('\xff\xfeG=lambda:map(int,input().split())\nG()\nprint(sum(a**b for a,b in zip(G(),G())))'))
# G=lambda:map(int,input().split())
# G()
# print(sum(a**b for a,b in zip(G(),G())))
