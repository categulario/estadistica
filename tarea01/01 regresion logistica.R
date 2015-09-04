library(class)

## Genera dos conjuntos de datos de entrenamiento de distintas clases dada una
## distribución normal y sus parámetros. A partir de ahí prueba dos
## clasificadores, uno con regresión logística y otro con k-nn pare determinar la
## clase de los datos de muestra.

# Generación de los datos de la clase 1
n1 <- 100                                                       # Tamaño de la muestra
m1 <- c(0, 0)                                                   # Media (Centro de los datos)
s1 <- c(1, 3)                                                   # Sigma (varianza (Radio de dispersión de los datos))
d1 <- cbind(rnorm(n1, m1[1], s1[1]), rnorm(n1, m1[2], s1[2]))   # Los datos en si
cla1 <- rep("1", n1)                                            # Etiquetas (repeat "1" n1 veces)

# Generación de los datos de la clase 2
n2 <- 100
m2 <- c(0, 0)
s2 <- c(3, 1)
d2 <- cbind(rnorm(n2, m2[1], s2[1]), rnorm(n2, m2[2], s2[2]))
cla2 <- rep("2", n2)

# Une ambos conjuntos de datos

train <- rbind(d1, d2)
cl <- factor(c(cla1, cla2))

# Grafica puntos

x11()
plot(d1, pch=20, xlim=c(-4, 4), ylim=c(-4, 4), main="Datos de entrenamiento")
points(d2, pch=20, col="red")

## Genera datos de prueba de las mismas distribuciones que los de entrenamiento
## y con los mismos parámetros

# Genera datos clase 1
n11 <- 200                                                        ## tamaño de muestra de la clase 1
d11 <- cbind(rnorm(n11, m1[1], s1[1]), rnorm(n11, m1[2], s1[2]))  ## genera datos clase 1
cla11 <- rep("1", n11)                                            ## etiqueta clase 1

# Genera datos clase 2
n22 <- 200
d22 <- cbind(rnorm(n22, m2[1], s2[1]), rnorm(n22, m2[2], s2[2]))
cla22 <- rep("2", n22)

# Une ambos conjuntos de datos

test<-rbind(d11,d22)
clte<- factor(c(cla11,cla22))

# Grafica puntos

x11()
plot(d11, pch=20, xlim=c(-4, 4), ylim=c(-4, 4), main="Datos de prueba")
points(d22, pch=20, col="red")

## Ahora creamos los clasificadores a partir de los conjuntos de prueba

# Clasificador k-nn

k <- 1

clhat <- knn(train, test, cl, k = k)
print("Knn success ratio")
sum(clte == clhat) / (n11 + n22)        # porcentaje de aciertos

# Clasificador regresión logística

model <- glm(cl ~ train,  family=binomial("logit"))

a <- rowSums(coefficients(model)[2:3] * test) + coefficients(model)[1]

aux1 <- exp(a)

clhat2 <- rep("1", n11 + n22)

clhat2[aux1 > 1] <- "2"

print("loglike success ratio")
sum(clte == clhat2) / (n11 + n22)  # Porcentaje de aciertos
