from flask import Flask,request,json,send_file
import pulp 
import numpy as np
import matplotlib.pyplot as plt

dir(pulp)

app = Flask(__name__)

@app.route('/api',methods=['GET'])
def index():
    return {
        'name':'Hello World'
    }

@app.route('/',methods=['POST'])
@app.route('/data',methods=['POST'])
@app.route('/api/data',methods=['POST'])
def create():
    # request_data = json.loads(request.data)
    # print(request_data)
    # maxmin = request_data['data']['maxmin']
    # xObj = request_data['data']['xObj']
    # yObj = request_data['data']['yObj']
    # todas = request_data['data']['names']

    # x = pulp.LpVariable('x', lowBound = 0)
    # y = pulp.LpVariable('y', lowBound = 0)

    # max_z = pulp.LpProblem("Maximaze_Z", pulp.LpMaximize)
    # min_z = pulp.LpProblem("Minimize_Z", pulp.LpMinimize)

    # xmax = 0
    # ymax = 0

    # for j in range(len(todas)):
    #     print(todas[j]['valorX'], todas[j]['valorY'],todas[j]['igualador'],todas[j]['resultado'])
    

    # if maxmin == "maximizar":
    #     max_z += float(xObj)*x + float(yObj)*y
    #     for t in range(len(todas)):
    #         if todas[t]['igualador'] == ">=":
    #             max_z += float(todas[t]['valorX'])*x + float(todas[t]['valorY'])*y >= float(todas[t]['resultado'])
    #         else:
    #             max_z += float(todas[t]['valorX'])*x + float(todas[t]['valorY'])*y <= float(todas[t]['resultado'])
    #         # if xmax < float(todas[t]['valorX']):
    #         #     xmax = float(todas[t]['valorX'])
    #         # elif ymax < float(todas[t]['valorY']):
    #         #     ymax = float(todas[t]['valor'])
    #     # print(max_z)
    #     max_z.solve()
    #     print('El valor de x' + str(x.varValue))
    #     print('El valor de y' + str(y.varValue))
        
    # else:
    #     min_z += float(xObj)*x + float(yObj)*y
    #     for t in range(len(todas)):
    #         if todas[t]['igualador'] == ">=":
    #             min_z += float(todas[t]['valorX'])*x + float(todas[t]['valorY'])*y >= float(todas[t]['resultado'])
    #         else:
    #             min_z += float(todas[t]['valorX'])*x + float(todas[t]['valorY'])*y <= float(todas[t]['resultado'])
    #         # if xmax < float(todas[t]['valorX']):
    #         #     xmax = float(todas[t]['valorX'])
    #         # elif ymax < float(todas[t]['valorY']):
    #         #     ymax = float(todas[t]['valorY'])
    #     # print(min_z)
    #     print(min_z.solve())
    #     print('El valor de x' + str(x.varValue))
    #     print('El valor de y' + str(y.varValue))


    # xmax = 2
    # ymax = 2
    # for t in range(len(todas)):
    #     xactual = float(todas[t]['valorX'])
    #     yactual = float(todas[t]['valorY'])
    #     resul = float(todas[t]['resultado'])
    #     if yactual != 0.0:
    #         maxEnY = (resul / yactual) + ((xactual/yactual)*-1)
    #         if maxEnY > ymax:
    #             ymax = int(maxEnY) + 10
    #     if xactual != 0.0:
    #         maxEnX = (resul / xactual) + ((yactual/xactual)*-1)
    #         if maxEnX > xmax:
    #             xmax = int(maxEnX) + 10

    # xfun = np.linspace(0,xmax + 10, 2000)
    # yval = []
    # pos = 0
    # for t in range(len(todas)):
    #     x1 = float(todas[t]['valorX']) * -1
    #     x2 = float(todas[t]['valorY'])
    #     resul = float(todas[t]['resultado'])
    #     if x2 != 0:
    #         resultado = (resul / x2) + ((x1 / x2)*xfun)
        
    #         yval.append(resultado)
    #         plt.plot(xfun, resultado, label = f"{str(x1 * -1)}x + {str(x2)}x2 {todas[t]['igualador']} {str(resul)}")
    #         if todas[t]['igualador'] == "<=":
    #             plt.fill_between(xfun, resultado, where = resultado <= resultado, alpha=0.5)
    #         elif todas[t]['igualador'] == ">=":
    #             plt.fill_between(xfun, resultado, where = resultado >= resultado, alpha=0.5)
    #     else:
    #         pos = 0 
    #         op = np.arange(2000) * 0
    #         resultado = resul / (x1 * -1)
    #         for b in range(len(xfun)):
    #             if resultado == xfun[b]:
    #                 op[b] = ymax + 10
    #                 pos = b
    #                 break
    #             if xfun[b] > resultado and b != 0:
    #                 op[b-1] = ymax + 10
    #                 pos = b - 1
    #                 break

    #         for c in range(len(op)):
    #             if todas[t]['igualador'] == "<=":
    #                 if c >= pos:
    #                     op[c] = ymax + 10
    #                 elif todas[t]['igualador'] == ">=":
    #                     if c <= pos:
    #                         op[c] = xmax + 10
            
    #         yval.append(op)
    #         plt.plot(xfun, op, label = f"{str(x1 * -1)}x + {str(x2)}x2 {todas[t]['igualador']} {str(resul)}")
    #         if todas[t]['igualador'] == "<=":
    #             plt.fill_between(xfun, op, where = op <= op , alpha = 0.5)
    #         elif todas[t]['igualador'] == ">=":
    #             plt.fill_between(xfun, op, where = op >= op , alpha = 0.5)
    # plt.plot(x.varValue, y.varValue, marker = "o", color = "k", label = 'Z')
    # plt.ylim(0, ymax)
    # plt.xlim(0, xmax)
    # plt.suptitle('x = '+str(x.varValue)+', y ='+str(y.varValue)+', Z ='+str(pulp.value(min_z.objective)), fontsize=10)
    
    # plt.legend()
    # plt.grid(True)
    # plt.plot()
    # plt.savefig('Ejemplo.png', bbox_inches='tight')
    return send_file('Ejemplo.png',mimetype='image/png')
    
    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) 