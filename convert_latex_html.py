c1 = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
<head>
<title>Mathedemo</title>
<style>
  body {
    font-size: 26px;
  }

  h1 {
    font-size: 36px;
  }

  h2 {
    font-size: 28px;
  }

  p {
    font-size: 20px;
  }
</style>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
</script>
<script type="text/javascript"
  src="http://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
</head>

<body>
'''

c2 = '''
</body>
</html>
'''

texto = '''

<h1> Matrix Similarity </h1>

<p>Let us start by deﬁning similar matrices:</p>

<p>Deﬁnition 1. Let A and B   e$n \times n$ matrices. If we can ﬁnd a non-singular$ n\tim  $ $n matrix P such</p>

$$
A = P^{-1} BP
$$
(1)

<p>then we say that A and B are similar to each other.</p>

<p>Note that (1) implies</p>

$$ \begin{matrix}{l}
PAP^{-1} = PP^{-1}BPP^{-1} \\
PAP^{-1} = IBI ⇒ (I is the n × n identity matrix )\\
B = P AP^{-1} \\
\end{matrix} $$

In other words, in declaring matrix similarity, it does not matter which matrix (A or B) is on the left hand side, 
and which gets multiplied with two other matrices.
'''


dna_repair = '''

<p> La reparación del ADN es el conjunto de procesos que usan las células para encontrar y corregir daños en el 
material 
genético. Los tres tipos principales de estos mecanismos son: la reparación por escisión de bases, la reparación por 
escisión de nucleótidos y la reparación de errores de apareamiento.</p>

<h1>Tipos de mecanismos</h1>

Escisión de bases: quita y 
cambia una sola letra o base dañada del ADN.Escisión de nucleótidos: saca un trozo más grande de ADN cuando hay 
lesiones que deforman la cadena, como las causadas por el sol.Errores de apareamiento: corrige las letras que no 
encajan bien durante la copia del ADN.Roturas dobles: arregla cuando la cadena de ADN se parte por completo usando 
unión de extremos o recombinación.Importancia para la saludProtección: frena los cambios malos o mutaciones que 
pueden causar cáncer.Equilibrio: ayuda a que el cuerpo y las células sigan funcionando bien todos los días.¿Quieres 
saber más sobre cómo se relaciona la reparación del ADN con el cáncer o prefieres explorar un tipo de daño en 
específico?

'''

file='textlatex.html'
fil = open(file, 'w')
  
fil.write(c1)
fil.write(texto)
fil.write(dna_repair)
fil.write(c2)
fil.close()
