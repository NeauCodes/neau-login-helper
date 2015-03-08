 #!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 2, 7

code          = {}
codeCount     = {}
codeWidth     = {}
codePrefix    = {}

codeLocPrefix = {
  "1" : 6,
  "2" : 19,
  "3" : 32,
  "4" : 45
}

codeHash = {
    "0" : "0",
    "1" : "1",
    "2" : "2",
    "3" : "3",
    "4" : "4",
    "5" : "5",
    "6" : "6",
    "7" : "7",
    "8" : "8",
    "9" : "9"
}

codeCount["0"]  = 42.0
codeWidth["0"]  = 8
codePrefix["0"] = 0
code["0"] = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 1, 0, 0],
[0, 0, 1, 1, 0, 1, 1, 0],
[0, 0, 1, 0, 0, 0, 1, 0],
[0, 1, 1, 0, 0, 0, 1, 1],
[0, 1, 1, 0, 0, 0, 1, 1],
[0, 1, 1, 0, 0, 0, 1, 1],
[0, 1, 1, 0, 0, 0, 1, 1],
[0, 1, 1, 0, 0, 0, 1, 1],
[0, 1, 1, 0, 0, 0, 1, 1],
[0, 0, 1, 0, 0, 0, 1, 0],
[0, 0, 1, 1, 0, 1, 1, 0],
[0, 0, 0, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]

codeCount["1"]  = 30.0
codeWidth["1"]  = 7
codePrefix["1"] = 0
code["1"] = [
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 1, 1, 0, 0],
[0, 0, 0, 1, 1, 0, 0],
[0, 0, 0, 1, 1, 0, 0],
[0, 0, 0, 1, 1, 0, 0],
[0, 0, 0, 1, 1, 0, 0],
[0, 0, 0, 1, 1, 0, 0],
[0, 0, 0, 1, 1, 0, 0],
[0, 0, 0, 1, 1, 0, 0],
[0, 0, 0, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0]
]

codeCount["2"]  = 36.0
codeWidth["2"]  = 8
codePrefix["2"] = 0
code["2"] = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 0, 0],
[0, 1, 0, 0, 1, 1, 1, 0],
[1, 0, 0, 0, 0, 1, 1, 0],
[0, 0, 0, 0, 0, 1, 1, 0],
[0, 0, 0, 0, 0, 1, 1, 0],
[0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 1, 1, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 1],
[0, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]

codeCount["3"]  = 37.0
codeWidth["3"]  = 7
codePrefix["3"] = 0
code["3"] = [
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 0],
[1, 1, 0, 0, 1, 1, 1],
[1, 0, 0, 0, 0, 1, 1],
[0, 0, 0, 0, 0, 1, 1],
[0, 0, 0, 0, 1, 1, 0],
[0, 0, 0, 1, 1, 1, 0],
[0, 0, 0, 0, 1, 1, 1],
[0, 0, 0, 0, 0, 1, 1],
[0, 0, 0, 0, 0, 1, 1],
[0, 0, 0, 0, 0, 1, 1],
[1, 1, 0, 0, 1, 1, 0],
[1, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0]
]

codeCount["4"]  = 36.0
codeWidth["4"]  = 8
codePrefix["4"] = 0
code["4"] = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 1, 0],
[0, 0, 0, 0, 0, 1, 1, 0],
[0, 0, 0, 0, 1, 1, 1, 0],
[0, 0, 0, 1, 0, 1, 1, 0],
[0, 0, 1, 0, 0, 1, 1, 0],
[0, 0, 1, 0, 0, 1, 1, 0],
[0, 1, 0, 0, 0, 1, 1, 0],
[1, 0, 0, 0, 0, 1, 1, 0],
[1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 1, 1, 0],
[0, 0, 0, 0, 0, 1, 1, 0],
[0, 0, 0, 0, 0, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]

codeCount["5"]  = 31.0
codeWidth["5"]  = 7
codePrefix["5"] = 0
code["5"] = [
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 1, 1],
[0, 0, 0, 1, 1, 1, 1],
[0, 0, 1, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 1, 1, 1],
[0, 0, 0, 0, 0, 1, 1],
[0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 1],
[0, 1, 0, 0, 0, 1, 0],
[0, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0]
]

codeCount["6"]  = 43.0
codeWidth["6"]  = 8
codePrefix["6"] = 0
code["6"] = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 1, 1],
[0, 0, 0, 1, 1, 1, 0, 0],
[0, 0, 1, 1, 0, 0, 0, 0],
[0, 1, 1, 0, 0, 0, 0, 0],
[0, 1, 0, 1, 1, 1, 0, 0],
[1, 1, 1, 0, 0, 1, 1, 0],
[1, 1, 0, 0, 0, 0, 1, 1],
[1, 1, 0, 0, 0, 0, 1, 1],
[1, 1, 0, 0, 0, 0, 1, 1],
[1, 1, 0, 0, 0, 0, 1, 1],
[0, 1, 1, 0, 0, 1, 1, 0],
[0, 0, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]

codeCount["7"]  = 24.0
codeWidth["7"]  = 9
codePrefix["7"] = 0
code["7"] = [
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 1, 1, 1, 1, 1, 1, 0],
[0, 1, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0]
]

codeCount["8"]  = 44.0
codeWidth["8"]  = 8
codePrefix["8"] = 0
code["8"] = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 0, 0],
[0, 1, 1, 0, 0, 0, 1, 0],
[1, 1, 0, 0, 0, 0, 1, 1],
[1, 1, 0, 0, 0, 0, 1, 1],
[0, 1, 1, 0, 0, 1, 1, 0],
[0, 0, 1, 1, 1, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 0, 0],
[0, 1, 0, 0, 0, 1, 1, 0],
[1, 1, 0, 0, 0, 0, 1, 1],
[1, 1, 0, 0, 0, 0, 1, 1],
[0, 1, 1, 0, 0, 0, 1, 0],
[0, 0, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]

codeCount["9"]  = 42.0
codeWidth["9"]  = 8
codePrefix["9"] = 0
code["9"] = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 0, 0],
[0, 1, 1, 0, 0, 1, 1, 0],
[1, 1, 0, 0, 0, 0, 1, 1],
[1, 1, 0, 0, 0, 0, 1, 1],
[1, 1, 0, 0, 0, 0, 1, 1],
[1, 1, 0, 0, 0, 0, 1, 1],
[0, 1, 1, 0, 0, 0, 1, 1],
[0, 0, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 1, 1, 0],
[0, 0, 0, 0, 1, 1, 0, 0],
[0, 0, 0, 1, 1, 0, 0, 0],
[1, 1, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]
