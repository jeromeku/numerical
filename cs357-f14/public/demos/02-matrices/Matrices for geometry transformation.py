
# coding: utf-8

# # Matrices to transform geometry

# In[7]:

import numpy as np
import matplotlib.pyplot as pt


# In[17]:

def parse_squiggle(s):
    numbers = [float(num) for num in s.split()]
    a = np.array(numbers)
    return a.reshape(-1, 2).T

stickman = parse_squiggle("251.43 286.38 250.93 286.27 250.55 286.04 250.67 286.61 250.93 286.95 251.31 287.29 251.94 287.63 252.44 287.86 253.33 288.09 254.08 288.32 255.09 288.54 256.11 288.66 257.24 288.77 258.76 289.11 260.02 289.23 261.54 289.45 262.67 289.57 263.94 289.57 264.82 289.68 265.71 289.68 266.59 289.79 267.09 289.79 267.60 289.91 268.23 290.13 268.61 290.36 269.12 290.70 269.62 290.93 270.13 291.04 270.76 291.04 271.26 291.04 271.64 291.04 271.26 291.04 271.39 290.70 271.64 290.13 272.02 289.34 272.40 288.43 273.16 287.07 273.79 286.04 274.42 284.68 275.31 282.97 275.94 281.04 276.69 278.77 277.58 276.38 278.21 274.11 279.09 272.17 279.85 270.81 280.23 269.56 280.99 268.76 281.49 267.85 282.00 266.83 282.63 265.69 283.01 264.44 283.52 263.08 284.27 261.60 285.28 260.24 286.04 258.87 286.67 257.96 287.05 257.39 287.18 257.17 287.56 257.17 287.94 257.62 288.44 258.08 288.82 258.99 289.20 260.35 289.83 261.71 290.08 263.31 290.46 264.67 290.97 265.92 291.60 267.17 292.11 268.42 292.61 269.67 293.24 271.15 293.62 272.63 294.13 274.11 294.63 275.36 294.88 276.61 295.39 277.74 295.89 278.65 296.27 279.56 296.65 280.24 296.91 280.81 297.16 281.38 297.66 282.18 298.17 282.86 298.55 283.43 298.93 283.88 299.05 284.22 299.31 284.56 299.56 285.13 299.94 285.59 300.06 285.93 300.32 286.27 300.57 286.61 300.82 286.95 301.07 287.29 301.33 287.63 301.33 287.97 301.45 288.43 301.58 288.77 301.83 289.23 302.08 289.57 302.59 289.91 302.97 290.13 303.22 290.48 303.47 290.93 303.73 291.39 304.23 291.73 304.61 292.18 304.74 292.64 305.12 293.09 305.49 293.55 305.87 293.77 306.25 294.00 306.63 294.23 306.51 293.89 307.01 293.66 307.39 293.55 307.89 293.43 308.53 293.32 309.03 293.20 309.54 292.98 310.29 292.75 311.18 292.41 312.32 292.18 313.45 291.95 314.59 291.73 315.73 291.61 316.99 291.39 318.38 291.27 319.52 291.04 320.78 290.93 321.79 290.82 322.80 290.70 323.81 290.48 324.44 290.48 325.20 290.36 325.58 290.25 326.21 290.13 326.72 290.02 327.35 289.91 327.85 289.91 328.23 289.79 328.48 289.45 328.48 288.77 328.48 287.97 328.48 286.84 328.48 285.25 328.36 283.88 328.23 282.29 327.73 280.47 327.35 278.31 326.59 276.15 326.08 273.99 325.45 271.95 324.95 270.13 324.44 268.42 324.06 266.94 323.68 265.47 323.31 263.99 322.93 262.62 322.67 261.37 322.42 260.35 322.17 259.21 321.92 258.42 321.66 257.39 321.41 256.48 321.16 255.69 321.03 254.89 320.91 253.98 320.78 253.30 320.53 252.28 320.40 251.71 320.27 250.80 320.02 250.12 319.89 249.44 319.77 248.75 319.52 248.19 319.39 247.62 319.26 247.28 319.14 246.71 319.01 246.25 318.88 245.80 318.76 245.46 318.63 245.12 318.51 244.21 318.51 243.75 318.38 243.18 318.25 242.50 318.00 242.05 317.75 241.36 317.62 240.68 317.62 240.00 317.49 239.66 317.37 239.32 317.24 238.98 317.24 238.64 317.12 238.18 316.99 237.73 316.99 237.16 316.86 236.59 316.74 236.13 316.61 235.34 316.48 234.77 316.23 234.09 316.11 233.41 315.85 232.84 315.73 232.38 315.60 231.93 315.47 231.59 315.09 230.91 314.84 230.56 314.72 230.22 314.46 229.65 314.21 229.43 313.96 228.97 313.71 228.29 313.33 227.61 313.07 226.93 312.69 226.36 312.57 226.02 312.32 225.56 312.06 224.99 312.06 224.43 311.81 223.97 311.68 223.52 311.56 223.17 311.43 222.83 311.31 222.27 311.18 221.92 311.18 221.36 311.05 220.90 310.93 220.22 310.80 219.65 310.67 219.08 310.55 218.40 310.42 217.72 310.17 217.15 310.04 216.35 309.79 215.67 309.66 215.44 309.54 215.10 309.54 214.76 309.54 214.42 309.16 214.42 309.16 213.97 309.54 213.97 310.17 213.97 310.67 213.97 311.18 214.19 311.68 214.42 312.06 214.53 312.44 214.65 312.95 214.76 313.45 214.76 313.96 214.88 314.46 215.10 314.97 215.22 315.35 215.44 315.98 215.67 316.61 215.67 317.49 216.01 318.25 216.13 318.88 216.24 319.52 216.35 320.02 216.47 320.53 216.69 321.03 216.81 321.41 216.92 321.79 217.04 322.42 217.15 322.80 217.38 323.18 217.38 323.56 217.38 324.06 217.38 324.57 217.38 325.07 217.49 325.58 217.49 326.08 217.72 326.59 217.83 327.09 217.95 327.60 218.06 327.98 218.06 328.48 218.40 329.24 218.63 330.25 218.85 331.14 219.08 331.77 219.08 332.27 219.08 332.78 219.20 333.16 219.20 333.54 219.20 333.92 219.20 334.55 219.42 335.05 219.42 335.81 219.54 336.57 219.54 337.33 219.54 337.83 219.54 338.46 219.54 339.09 219.65 339.47 219.76 340.11 219.76 340.48 219.76 340.86 219.76 341.24 219.76 341.62 219.76 342.00 219.76 342.63 219.88 343.26 219.99 343.77 220.11 344.27 220.22 344.65 220.33 345.03 220.33 345.54 220.45 345.79 220.11 345.92 219.65 346.04 218.97 346.29 218.06 346.42 216.81 346.80 215.90 346.93 214.76 347.18 213.63 347.31 212.26 347.43 211.24 347.56 210.10 347.68 208.96 347.81 207.94 347.94 206.69 347.94 205.44 348.06 204.42 348.06 203.39 348.19 202.37 348.32 201.57 348.32 200.67 348.44 200.10 348.44 199.53 348.44 199.19 348.32 198.85 348.32 198.51 348.32 198.16 348.32 197.82 348.32 197.25 348.32 196.57 348.32 196.23 348.32 195.78 348.32 195.44 347.94 195.66 347.43 195.66 347.05 195.66 346.55 195.55 345.66 195.55 344.78 195.55 343.77 195.44 342.76 195.32 341.75 195.09 340.61 194.87 339.35 194.53 338.21 194.30 336.82 193.96 335.43 193.73 334.17 193.39 332.91 193.05 331.64 192.82 330.25 192.59 328.99 192.25 327.47 192.03 326.21 191.68 324.82 191.34 323.56 190.89 322.29 190.43 321.03 189.98 319.77 189.64 318.63 189.41 317.49 189.18 316.36 188.96 315.35 188.73 314.72 188.50 313.96 188.27 313.58 188.16 313.20 188.05 312.69 187.93 312.06 187.82 311.56 187.82 311.18 187.71 310.67 187.59 310.29 187.48 309.79 187.48 309.41 187.36 309.03 187.36 308.40 187.36 307.89 187.25 307.39 187.14 306.76 187.14 306.25 187.02 305.87 186.91 305.49 186.91 305.12 186.68 304.74 186.68 304.36 186.45 304.36 186.80 304.74 186.80 305.37 186.91 306.00 187.02 306.51 187.25 307.26 187.48 308.02 187.71 308.78 187.93 309.41 188.05 309.92 188.16 310.67 188.27 311.18 188.27 311.81 188.39 312.32 188.39 312.95 188.39 313.45 188.39 313.96 188.39 314.59 188.27 315.22 187.93 315.60 187.71 315.98 187.59 316.36 187.36 316.74 187.25 317.37 186.68 317.75 186.45 318.13 186.11 318.63 185.55 319.01 185.20 319.39 184.75 319.77 184.18 320.27 183.61 320.40 183.16 320.91 182.59 321.28 182.02 321.54 181.23 321.79 180.54 321.92 179.86 322.04 178.95 322.17 178.16 322.29 177.25 322.42 176.34 322.55 175.43 322.67 174.52 322.67 173.49 322.80 172.59 322.80 171.79 322.80 171.11 322.67 170.43 322.67 169.52 322.55 168.72 322.29 167.70 321.92 166.67 321.41 165.76 321.03 164.51 320.53 163.60 320.15 162.69 319.77 161.79 319.26 160.99 318.63 159.97 318.00 159.17 317.49 158.26 316.99 157.24 316.36 156.33 315.85 155.42 314.97 154.28 314.21 153.49 313.58 152.58 312.69 151.78 311.81 150.76 310.80 149.73 309.54 148.71 308.65 147.69 307.64 146.78 306.63 145.98 305.75 145.19 304.74 144.51 303.60 143.94 302.46 143.14 301.33 142.57 299.94 141.89 298.67 141.09 297.41 140.41 296.02 139.62 294.63 138.93 293.12 138.37 291.35 137.80 289.45 137.34 287.43 136.89 285.54 136.43 283.89 136.09 282.38 135.87 280.99 135.52 279.98 135.30 278.84 135.18 277.83 135.07 276.95 134.96 275.81 134.96 274.93 134.96 273.79 134.96 272.65 134.96 271.52 135.07 270.38 135.30 269.37 135.64 268.36 135.98 267.35 136.55 266.72 137.00 265.71 137.46 265.07 137.91 264.44 138.25 263.68 138.71 263.05 139.16 262.17 139.84 261.54 140.41 260.78 140.87 260.15 141.44 259.64 142.00 259.14 142.57 258.63 143.25 258.00 143.82 257.49 144.62 256.99 145.53 256.48 146.44 255.98 147.35 255.47 148.26 255.09 148.94 254.59 149.73 254.34 150.76 253.96 151.55 253.58 152.69 253.33 153.83 253.07 154.74 252.95 155.76 252.95 156.90 252.82 158.03 252.82 159.40 252.69 160.53 252.69 161.79 252.69 162.81 252.69 163.83 252.82 164.85 252.95 165.88 253.07 166.79 253.20 167.70 253.45 168.49 253.71 169.29 253.96 170.08 254.21 170.88 254.34 171.68 254.46 172.36 254.59 172.93 254.72 173.49 254.84 174.29 254.97 174.97 255.09 175.65 255.22 176.45 255.47 177.13 255.73 177.93 255.98 178.61 256.36 179.41 256.61 179.97 256.99 180.54 257.37 181.23 257.75 181.79 258.00 182.48 258.25 182.93 258.63 183.61 258.88 183.95 259.26 184.41 259.64 184.75 260.40 184.98 260.91 185.20 261.54 185.43 262.17 185.66 262.55 186.00 263.05 186.23 263.68 186.57 264.32 186.80 265.07 187.02 265.83 187.36 266.59 187.48 267.35 187.59 268.11 187.71 268.86 187.71 269.75 187.71 270.88 187.93 271.77 188.05 272.78 188.16 273.79 188.27 274.80 188.27 275.81 188.27 276.44 188.27 276.82 188.39 277.20 188.50 277.58 188.61 277.71 188.96 277.33 188.84 276.95 188.84 276.44 188.84 275.94 188.73 275.56 188.61 275.18 188.61 274.80 188.61 274.29 188.61 273.66 188.61 273.28 188.61 272.53 188.73 271.89 188.73 271.14 188.84 270.25 188.84 269.37 189.07 268.48 189.30 267.47 189.52 266.59 189.87 265.96 189.98 265.07 190.21 264.44 190.32 263.68 190.43 262.93 190.55 262.17 190.55 261.28 190.55 260.65 190.66 259.89 190.89 259.26 191.00 258.51 191.12 257.62 191.23 256.74 191.46 255.98 191.57 255.35 191.91 254.84 192.14 254.34 192.37 253.96 192.48 253.33 192.71 252.82 192.82 252.32 193.05 251.94 193.05 251.43 193.28 250.80 193.39 250.29 193.62 249.54 193.96 249.03 194.30 248.40 194.53 247.77 194.75 247.26 194.87 246.63 195.21 246.00 195.55 245.62 195.89 245.24 196.23 244.86 196.46 244.48 196.57 244.11 196.80 243.60 197.14 242.97 197.60 242.59 197.82 242.08 197.94 241.71 198.05 241.20 198.28 240.69 198.62 240.19 198.96 239.81 199.19 239.43 199.41 238.93 199.53 238.55 199.76 237.92 199.87 237.54 199.98 237.16 199.98 236.78 200.32 236.53 200.67 236.53 201.23 236.65 201.80 236.78 202.48 237.03 202.83 237.28 203.51 237.79 204.42 238.29 205.21 238.67 206.35 239.18 207.26 239.43 208.05 239.81 208.74 240.19 209.31 240.57 209.99 241.07 210.67 241.45 211.35 241.83 212.15 242.34 212.83 242.46 213.17 242.72 213.63 242.97 213.97 243.22 214.65 243.35 214.99 243.47 215.33 243.60 215.90 243.73 216.47 243.85 216.81 244.11 217.26 244.36 217.49 244.36 217.95 244.61 218.40 244.86 218.74 244.99 219.08 245.12 219.42 245.49 219.54 245.87 219.54 246.38 219.54 246.76 219.54 247.26 219.54 247.77 219.54 248.53 219.54 249.03 219.65 249.79 219.65 250.55 219.54 251.31 219.54 252.06 219.54 252.82 219.54 253.45 219.42 254.21 219.42 254.97 219.20 255.60 219.20 256.36 219.08 256.86 218.85 257.37 218.74 257.75 218.74 258.38 218.63 258.88 218.51 259.64 218.40 260.27 218.29 260.91 218.17 261.41 218.06 261.79 217.95 262.17 217.95 262.80 217.83 263.31 217.72 263.94 217.49 264.44 217.38 264.82 217.38 265.33 217.26 265.96 217.04 266.46 217.04 267.22 216.92 267.85 216.81 268.36 216.69 269.24 216.58 269.62 216.47 270.25 216.35 270.88 216.24 271.39 216.13 271.89 216.13 272.53 216.01 273.03 216.01 273.79 216.01 274.42 216.01 275.31 215.90 275.94 215.90 276.44 215.67 276.95 215.67 277.58 215.67 277.96 215.56 278.46 215.44 278.97 215.44 279.73 215.56 280.48 215.67 281.24 215.67 281.87 215.67 282.38 215.67 282.76 215.67 283.39 215.67 284.02 215.67 284.53 215.67 285.16 215.67 285.54 215.67 286.04 215.90 286.29 216.24 285.92 216.58 285.66 217.04 285.41 217.72 284.78 218.29 284.15 219.08 283.52 219.99 282.63 220.56 282.00 221.58 281.12 222.27 280.36 223.06 279.98 223.97 279.47 224.43 279.09 224.99 278.46 225.56 277.83 226.02 277.33 226.81 276.82 227.49 276.57 228.29 276.32 228.86 275.94 229.31 275.56 229.65 275.18 230.00 274.67 230.56 274.42 231.02 274.04 231.36 273.79 231.93 273.54 232.38 273.28 233.07 272.91 233.97 272.27 234.66 271.77 235.45 271.39 236.02 271.01 236.48 270.88 237.04 270.63 237.50 270.51 238.07 270.25 238.75 270.00 239.20 269.75 239.77 269.62 240.00 269.49 240.68 269.37 241.25 269.24 241.71 268.99 242.39 268.74 242.96 268.48 243.75 268.11 244.55 267.85 245.23 267.47 246.25 267.22 246.93 266.97 247.96 266.59 248.64 266.34 249.21 266.08 249.78 265.83 250.12 265.58 250.46 265.45 251.03 265.20 251.37 264.95 251.71 264.69 252.05 264.57 252.51 264.32 252.85 264.06 253.30 263.94 253.76 263.56 254.32 263.18 254.78 262.93 255.12 262.55 255.46 262.17 255.69 261.92 256.14 261.66 256.60 261.54 257.05 261.28 257.62 260.91 258.08 260.53 258.64 260.27 259.10 259.89 259.44 259.64 259.89 259.39 260.24 259.14 260.58 258.88 260.92 258.76 261.49 258.38 262.28 258.13 262.62 257.87 263.31 257.62 263.76 257.37 264.33 257.24 264.90 256.99 265.47 256.74 266.03 256.48 266.60 256.23 267.17 256.11 267.51 255.85 267.85 255.73 268.31 255.47 268.76 255.22 269.22 255.09 269.90 254.84 270.35 254.59 270.92 254.34 271.38 254.08 271.83 253.96 272.29 253.83 272.74 253.58 273.08 253.33 273.88 253.33 274.33 253.20 274.79 253.20 275.36 252.95 276.04 252.69 276.38 252.57 276.95 252.44 277.40 252.32 277.86 252.32 278.31 252.19 278.77 252.06 279.22 251.94 279.56 251.81 280.02 251.56 280.59 251.43 281.27 251.43 281.61 251.31 281.84 251.18 282.29 251.05 282.75 251.05 283.09 250.80 283.54 250.67 283.88 250.67 284.22 250.55 284.68 250.55 285.13 250.42 285.59 250.29 285.93 250.29 286.27 250.29 286.61 250.42 286.04 250.93 284.45")
stickman[1] *= -1


# In[15]:

pt.plot(stickman[0], stickman[1])


# Now define A to be a rotation matrix: (Use geometric intuition!)

# In[18]:

alpha = 0.1*np.pi


# In[19]:

A = np.array([
    [np.cos(alpha), np.sin(alpha)],
    [-np.sin(alpha), np.cos(alpha)]
])


# Now multiply the geometry by this matrix, reassign to `stickman`, and plot:

# In[39]:

stickman = np.einsum("ij,jk->ik", A, stickman)
pt.plot(stickman[0], stickman[1])


# In[ ]:


