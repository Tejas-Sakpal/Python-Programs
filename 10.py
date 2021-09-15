Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from pulp import *
>>> factory=["F1","F2","F3"]
>>> supply={"F1":7,"F2":9,"F3":18}
>>> warehouse=["W1","W2","W3","W4"}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> warehouse=["W1","W2","W3","W4"]
>>> required={"W1":5,"W2":8,"W3":7,"W4":14}
>>> costs={"F1":{"W1":19,"W2":30,"W3":50,"W4":10},
       "F2":{"W1":70,"W2":30,"W3":40,"W4":60},
       "F3":{"W1":40,"W2":8,"W3":70,"W4":20}}
>>> prob=LpProblem("Transportation",LpMinimize)
>>> Routes=[(w,r) for w in factory for r in warehouse]
>>> vars=LpVariable.dicts("Route",(factory,warehouse),0,None,LpInteger)
>>> prob+=lpSum([vars[w][r]*costs[w][r] for (w,r) in Routes]),"Sum_of_Costs
SyntaxError: EOL while scanning string literal
>>> prob+=lpSum([vars[w][r]*costs[w][r] for (w,r) in Routes]),"Sum_of_Costs
SyntaxError: EOL while scanning string literal
>>> prob+=lpSum([vars[w][r]*costs[w][r] for (w,r) in
	     Routes]),"Sum_of_Costs
SyntaxError: EOL while scanning string literal
>>> prob+=lpSum([vars[w][r]*costs[w][r] for (w,r) in Routes]),"Sum_of_Costs"
>>> for w in factory:
	prob+=lpSum([vars[w][r] for r in warehouse])<=supply[w],"Sum_Prod_%s"%w

	
>>> for r in warehouse:
	prob+=lpSum([vars[w][r] for w in factory])>=required[r],"Sum_Prod_%s"%r

	
>>> prob.writeLP
<bound method LpProblem.writeLP of Transportation:
MINIMIZE
19*Route_F1_W1 + 30*Route_F1_W2 + 50*Route_F1_W3 + 10*Route_F1_W4 + 70*Route_F2_W1 + 30*Route_F2_W2 + 40*Route_F2_W3 + 60*Route_F2_W4 + 40*Route_F3_W1 + 8*Route_F3_W2 + 70*Route_F3_W3 + 20*Route_F3_W4 + 0
SUBJECT TO
Sum_Prod_F1: Route_F1_W1 + Route_F1_W2 + Route_F1_W3 + Route_F1_W4 <= 7

Sum_Prod_F2: Route_F2_W1 + Route_F2_W2 + Route_F2_W3 + Route_F2_W4 <= 9

Sum_Prod_F3: Route_F3_W1 + Route_F3_W2 + Route_F3_W3 + Route_F3_W4 <= 18

Sum_Prod_W1: Route_F1_W1 + Route_F2_W1 + Route_F3_W1 >= 5

Sum_Prod_W2: Route_F1_W2 + Route_F2_W2 + Route_F3_W2 >= 8

Sum_Prod_W3: Route_F1_W3 + Route_F2_W3 + Route_F3_W3 >= 7

Sum_Prod_W4: Route_F1_W4 + Route_F2_W4 + Route_F3_W4 >= 14

VARIABLES
0 <= Route_F1_W1 Integer
0 <= Route_F1_W2 Integer
0 <= Route_F1_W3 Integer
0 <= Route_F1_W4 Integer
0 <= Route_F2_W1 Integer
0 <= Route_F2_W2 Integer
0 <= Route_F2_W3 Integer
0 <= Route_F2_W4 Integer
0 <= Route_F3_W1 Integer
0 <= Route_F3_W2 Integer
0 <= Route_F3_W3 Integer
0 <= Route_F3_W4 Integer
>
>>> prob.solve()
1
>>> value(prob.objective)
743.0
>>> for v in prob.variables():
	print(v.name,"=",v.varValue)

	
Route_F1_W1 = 5.0
Route_F1_W2 = 0.0
Route_F1_W3 = 0.0
Route_F1_W4 = 2.0
Route_F2_W1 = 0.0
Route_F2_W2 = 2.0
Route_F2_W3 = 7.0
Route_F2_W4 = 0.0
Route_F3_W1 = 0.0
Route_F3_W2 = 6.0
Route_F3_W3 = 0.0
Route_F3_W4 = 12.0
>>> 
================================ RESTART: Shell ================================
>>> from pulp import *
>>> factory=["A","B","C","D"]
>>> supply={"A":50,"B":70,"C":30,"D":50}
>>> stores=["I","II","III","IV"]
>>> demand={"I":25,"II":35,"III":105,"IV":20}
>>> costs={"A":{"I":4,"II":6,"III":8,"IV":13},
       "B":{"I":13,"II":11,"III":10,"IV":8},
       "C":{"I":14,"II":4,"III":10,"IV":13},
       "D":{"I":9,"II":11,"III":13,"IV":8}}
>>> prob=LpProblem("Transportation",LpMinimize)
>>> Routes=[(w,r) for w in factory for r in stores]
>>> vars=LpVariable.dicts("Route",(factory,stores),0,None,LpInteger)
>>> prob+=lpSum([vars[w][r]*costs[w][r] for (w,r) in Routes]),"Sum_of_costs"
>>> for w in factory:
	prob+=lpSum([vars[w][r] for r in stores])<=supply[w],"Sum_Prod_%s"%w

	
>>> for r in stores:
	prob+=lpSum([vars[w][r] for w in factory])>=demand[r],"Sum_Prod_%s"%r

	
>>> prob.writeLP
<bound method LpProblem.writeLP of Transportation:
MINIMIZE
4*Route_A_I + 6*Route_A_II + 8*Route_A_III + 13*Route_A_IV + 13*Route_B_I + 11*Route_B_II + 10*Route_B_III + 8*Route_B_IV + 14*Route_C_I + 4*Route_C_II + 10*Route_C_III + 13*Route_C_IV + 9*Route_D_I + 11*Route_D_II + 13*Route_D_III + 8*Route_D_IV + 0
SUBJECT TO
Sum_Prod_A: Route_A_I + Route_A_II + Route_A_III + Route_A_IV <= 50

Sum_Prod_B: Route_B_I + Route_B_II + Route_B_III + Route_B_IV <= 70

Sum_Prod_C: Route_C_I + Route_C_II + Route_C_III + Route_C_IV <= 30

Sum_Prod_D: Route_D_I + Route_D_II + Route_D_III + Route_D_IV <= 50

Sum_Prod_I: Route_A_I + Route_B_I + Route_C_I + Route_D_I >= 25

Sum_Prod_II: Route_A_II + Route_B_II + Route_C_II + Route_D_II >= 35

Sum_Prod_III: Route_A_III + Route_B_III + Route_C_III + Route_D_III >= 105

Sum_Prod_IV: Route_A_IV + Route_B_IV + Route_C_IV + Route_D_IV >= 20

VARIABLES
0 <= Route_A_I Integer
0 <= Route_A_II Integer
0 <= Route_A_III Integer
0 <= Route_A_IV Integer
0 <= Route_B_I Integer
0 <= Route_B_II Integer
0 <= Route_B_III Integer
0 <= Route_B_IV Integer
0 <= Route_C_I Integer
0 <= Route_C_II Integer
0 <= Route_C_III Integer
0 <= Route_C_IV Integer
0 <= Route_D_I Integer
0 <= Route_D_II Integer
0 <= Route_D_III Integer
0 <= Route_D_IV Integer
>
>>> prob.solve()
1
>>> value(prob.objective)
1465.0
>>> for v in prob.variables():
	print(v.name,"=",v.varValue)

	
Route_A_I = 10.0
Route_A_II = 5.0
Route_A_III = 35.0
Route_A_IV = 0.0
Route_B_I = 0.0
Route_B_II = 0.0
Route_B_III = 70.0
Route_B_IV = 0.0
Route_C_I = 0.0
Route_C_II = 30.0
Route_C_III = 0.0
Route_C_IV = 0.0
Route_D_I = 15.0
Route_D_II = 0.0
Route_D_III = 0.0
Route_D_IV = 20.0
>>> 
================================ RESTART: Shell ================================
>>> from pulp import *
>>> origin=["A","B","C"]
>>> available={"A":60,"B":70,"C":80}
>>> destination=["X","Y","Z"]
>>> requirement={"X":50,"Y":80,"Z":80}
>>> costs={"A":{"X":8,"Y":7,"Z":3},
       "B":{"X":3,"Y":8,"Z":9},
       "C":{"X":11,"Y":3,"Z":5}}
>>> prob=LpProblem("Transportation",LpMinimize)
>>> Routes=[(w,r) for w in origin for r in destination]
>>> vars=LpVariable.dicts("Route",(origin,destination),0,None,LpInteger)
>>> prob+=lpSum([vars[w][r]*costs[w][r] for (w,r) in Routes]),"Sum_of_costs"
>>> for w in origin:
	prob+=lpSum([vars[w][r] for r in destination])<=available[w],"Sum_Prod_%s"%w

	
>>> for r in destination:
	prob+=lpSum([vars[w][r] for w in origin])>=requirement[r],"Sum_Prod_%s"%r

	
>>> prob.writeLP
<bound method LpProblem.writeLP of Transportation:
MINIMIZE
8*Route_A_X + 7*Route_A_Y + 3*Route_A_Z + 3*Route_B_X + 8*Route_B_Y + 9*Route_B_Z + 11*Route_C_X + 3*Route_C_Y + 5*Route_C_Z + 0
SUBJECT TO
Sum_Prod_A: Route_A_X + Route_A_Y + Route_A_Z <= 60

Sum_Prod_B: Route_B_X + Route_B_Y + Route_B_Z <= 70

Sum_Prod_C: Route_C_X + Route_C_Y + Route_C_Z <= 80

Sum_Prod_X: Route_A_X + Route_B_X + Route_C_X >= 50

Sum_Prod_Y: Route_A_Y + Route_B_Y + Route_C_Y >= 80

Sum_Prod_Z: Route_A_Z + Route_B_Z + Route_C_Z >= 80

VARIABLES
0 <= Route_A_X Integer
0 <= Route_A_Y Integer
0 <= Route_A_Z Integer
0 <= Route_B_X Integer
0 <= Route_B_Y Integer
0 <= Route_B_Z Integer
0 <= Route_C_X Integer
0 <= Route_C_Y Integer
0 <= Route_C_Z Integer
>
>>> prob.solve()
1
>>> value(prob.objective)
750.0
>>> for v in prob.variables():
	print(v.name,"=",v.varValue)

	
Route_A_X = 0.0
Route_A_Y = 0.0
Route_A_Z = 60.0
Route_B_X = 50.0
Route_B_Y = 0.0
Route_B_Z = 20.0
Route_C_X = 0.0
Route_C_Y = 80.0
Route_C_Z = 0.0
>>> 
================================ RESTART: Shell ================================
>>> from pulp import *
>>> jobs=["1","2","3","4","5"]
>>> supply={"1":1,"2":1,"3":1,"4":1,"5":1}
>>> machines=["I","II","III","IV","V"}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> machines=["I","II","III","IV","V"]
>>> requirement={"I":1,"II":1,"III":1,"IV":1,"V":1}
>>> costs={"1":{"I":3,"II":8,"III":2,"IV":10,"V":3},
       "2":{"I":8,"II":7,"III":2,"IV":9,"V":7},
       "3":{"I":6,"II":4,"III":2,"IV":7,"V":5},
       "4":{"I":8,"II":4,"III":2,"IV":3,"V":5},
       "5":{"I":9,"II":10,"III":6,"IV":9,"V":10}}
>>> prob=LpProblem("Assignment_Problem",LpMinimize)
>>> Routes=[(w,r) for w in jobs for r in machines]
>>> vars=LpVariable.dicts("Route",(jobs,machines),0,None,LpInteger)
>>> prob+=lpSum([vars[w][r]*costs[w][r] for (w,r) in Routes]),"Sum_of_Costs"
>>> for w in jobs:
	prob+=lpSum([vars[w][r] for r in machines])<=supply[w],"Sum_Prod_%s"%w

	
>>> for r in machines:
	prob+=lpSum([vars[w][r] for w in jobs])>=requirement[r],"Sum_Prod_%s"%r

	
>>> print(prob.writeLP)

>>> prob.solve()
1
>>> value(prob.objective)
21.0
>>> for v in prob.variables():
	print(v.name,"=",v.varValue)

	
Route_1_I = 0.0
Route_1_II = 0.0
Route_1_III = 0.0
Route_1_IV = 0.0
Route_1_V = 1.0
Route_2_I = 0.0
Route_2_II = 0.0
Route_2_III = 1.0
Route_2_IV = 0.0
Route_2_V = 0.0
Route_3_I = 0.0
Route_3_II = 1.0
Route_3_III = 0.0
Route_3_IV = 0.0
Route_3_V = 0.0
Route_4_I = 0.0
Route_4_II = 0.0
Route_4_III = 0.0
Route_4_IV = 1.0
Route_4_V = 0.0
Route_5_I = 1.0
Route_5_II = 0.0
Route_5_III = 0.0
Route_5_IV = 0.0
Route_5_V = 0.0
>>> 
================================ RESTART: Shell ================================
>>> from pulp import *
>>> jobs=["A","B","C","D"]
>>> supply={"A":1,"B":1,"C":1,"D":1}
>>> person=["I","II","III"]
>>> requirement={"I":1,"II":1,"III":1}
>>> costs={"A":{"I":7,"II":3,"III":5},
       "B":{"I":2,"II":7,"III":4},
       "C":{"I":6,"II":5,"III":3},
       "D":{"I":3,"II":4,"III":7}}
>>> prob=LpProblem("Assignment_Problem",LpMinimize)
>>> Routes=[(w,r) for w in jobs for r in person]
>>> vars=LpVariable.dicts("Route",(jobs,person),0,None,LpInteger)
>>> prob+=lpSum([vars[w][r]*costs[w][r] for (w,r) in Routes]),"Sum_of_Costs"
>>> for w in jobs:
	prob+=lpSum([vars[w][r] for r in person])<=supply[w],"Sum_Prod_%s"%w

	
>>> for r in person:
	prob+=lpSum([vars[w][r] for w in jobs])>=requirement[r],"Sum_Prod_%s"%r

	
>>> prob.writeLP
<bound method LpProblem.writeLP of Assignment_Problem:
MINIMIZE
7*Route_A_I + 3*Route_A_II + 5*Route_A_III + 2*Route_B_I + 7*Route_B_II + 4*Route_B_III + 6*Route_C_I + 5*Route_C_II + 3*Route_C_III + 3*Route_D_I + 4*Route_D_II + 7*Route_D_III + 0
SUBJECT TO
Sum_Prod_A: Route_A_I + Route_A_II + Route_A_III <= 1

Sum_Prod_B: Route_B_I + Route_B_II + Route_B_III <= 1

Sum_Prod_C: Route_C_I + Route_C_II + Route_C_III <= 1

Sum_Prod_D: Route_D_I + Route_D_II + Route_D_III <= 1

Sum_Prod_I: Route_A_I + Route_B_I + Route_C_I + Route_D_I >= 1

Sum_Prod_II: Route_A_II + Route_B_II + Route_C_II + Route_D_II >= 1

Sum_Prod_III: Route_A_III + Route_B_III + Route_C_III + Route_D_III >= 1

VARIABLES
0 <= Route_A_I Integer
0 <= Route_A_II Integer
0 <= Route_A_III Integer
0 <= Route_B_I Integer
0 <= Route_B_II Integer
0 <= Route_B_III Integer
0 <= Route_C_I Integer
0 <= Route_C_II Integer
0 <= Route_C_III Integer
0 <= Route_D_I Integer
0 <= Route_D_II Integer
0 <= Route_D_III Integer
>
>>> prob.solve()
1
>>> value(prob.objective)
8.0
>>> for v in prob.variables():
	print(v.name,"=",v.varValue)

	
Route_A_I = 0.0
Route_A_II = 1.0
Route_A_III = 0.0
Route_B_I = 1.0
Route_B_II = 0.0
Route_B_III = 0.0
Route_C_I = 0.0
Route_C_II = 0.0
Route_C_III = 1.0
Route_D_I = 0.0
Route_D_II = 0.0
Route_D_III = 0.0
>>> 
================================ RESTART: Shell ================================
>>> from pulp import *
>>> jobs=["1","2","3","4","5"]
>>> supply={"1":1,"2":1,"3":1,"4":1,"5":1}
>>> machines=["A","B","C","D","E"]
>>> requirement={"A":1,"B":1,"C":1,"D":1,"E":1}
>>> costs={"1":{"A":30,"B":37,"C":40,"D":28,"E":40},
       "2":{"A":40,"B":24,"C":27,"D":21,"E":36},
       "3":{"A":40,"B":32,"C":33,"D":30,"E":35},
       "4":{"A":25,"B":38,"C":40,"D":36,"E":36},
       "5":{"A":29,"B":32,"C":41,"D":34,"E":39}}
>>> prob=LpProblem("Assignment_Problem",LpMaximize)
>>> Routes=[(w,r) for w in jobs for r in machines]
>>> vars=LpVariable.dicts("Route",(jobs,machines),0,None,LpInteger)
>>> prob+=lpSum([vars[w][r]*costs[w][r] for (w,r) in Routes]),"Sum_of_Costs"
>>> for w in jobs:
	prob+=lpSum([vars[w][r] for r in machines])<=supply[w],"Sum_of_Prod_%s"%w

	
>>> for r in machines:
	prob+=lpSum([vars[w][r] for w in jobs])>=requirement[r],"Sum_of_Prod_%s"%r

	
>>> prob.writeLP

>>> prob.solve()
1
>>> print('Maximum Profit',"=",value(prob.objective))
Maximum Profit = 190.0
>>> for v in prob.variables():
	if v.varValue>0:
		print(v.name,"=",v.varValue)

		
Route_1_B = 1.0
Route_2_E = 1.0
Route_3_A = 1.0
Route_4_D = 1.0
Route_5_C = 1.0
>>> 