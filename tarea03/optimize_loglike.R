# Read data from files
x_data <- as.matrix(read.table('predictor.data'))
y_data <- read.table('observed.data')

# compute rows
x_rows <- length(x_data[,1])

# vector of ones
v <- rep(1, x_rows)

# extended x_data with ones
x_data <- cbind(v, x_data)

# number of columns
x_cols <- length(x_data[1,])

# This function returns the loglikelihood to be minimized
makeLogLike <- function(x_data, y_data) {
  # Loglike takes ß and is bound to x_data and y_data
  logLike <- function(ß) {
    acum <- 0
    for (i in 1:x_rows) {
      dot <- ß %*% x_data[i,]

      if (y_data[i,1] == 1) {
        acum <- acum + (dot - log(1 + exp(dot)))
      } else {
        acum <- acum + (-log(1 + exp(dot)))
      }
    }
    acum
  }
  logLike
}

# Make a loglike function from data
logLike <- makeLogLike(x_data, y_data)

# optimize loglike function
print(optim(rep(0, x_cols), logLike, control=list(fnscale = -1)))
