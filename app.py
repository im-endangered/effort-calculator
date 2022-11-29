from flask import Flask, redirect, url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/result/<string:O>/<string:APlus>/<string:A>/<string:BPlus>/<string:B>/<string:C>')
def result(O,APlus,A,BPlus,B,C):    
    
    
    return render_template('result.html',O=O,APlus=APlus,A=A,BPlus=BPlus,B=B,C=C)
        
@app.route('/check/')
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        fm=request.form.get('fullMarks')
        internal=request.form.get('internal')    
    full_marks=float(fm)
    internal_marks=float(internal)
    print(type(full_marks))
    print(type(internal_marks))
    if full_marks==100:
        O=(91-internal_marks)*2
        APlus=(81-internal_marks)*2
        A=(71-internal_marks)*2
        BPlus=(61-internal_marks)*2
        B=(56-internal_marks)*2
        C=(50-internal_marks)*2
    if full_marks==75:
        O=(91-internal_marks)*1.5
        APlus=(81-internal_marks)*1.5
        A=(71-internal_marks)*1.5
        BPlus=(61-internal_marks)*1.5
        B=(56-internal_marks)*1.5
        C=(50-internal_marks)*1.5  
    O= "{:.2f}".format(O)
    APlus= "{:.2f}".format(APlus)
    A= "{:.2f}".format(A)
    BPlus= "{:.2f}".format(BPlus)
    B= "{:.2f}".format(B)
    C= "{:.2f}".format(C)
    if float(O)>full_marks:
        O="Not possible"
    if float(APlus)>full_marks:
        APlus="Not possible"
    if float(A)>full_marks:
        A="Not possible"
    if float(BPlus)>full_marks:
        BPlus="Not possible"
    if float(B)>full_marks:
        B="Not possible"
    if float(C)>full_marks:
        C="Not possible"
    
    return redirect(url_for('result',O=O,APlus=APlus,A=A,BPlus=BPlus,B=B,C=C))
    # return convertedGrade
    
if __name__=='__main__':
    app.run(debug=True)