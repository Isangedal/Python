const fs = require("fs")
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const presetFile = "../Presets/encryption.txt"

encryption1_backup = [null, {"M": "1", "B": "1?", "Y": "1!"},  {"A": "2", "N": "2?", "T": "2!"},  {"O": "3", "H": "3?", "U": "3!"},  {"I": "4", "F": "4?", "S": "4!"},  {"Q": "5", "X": "5?", "R": "5!"},  {"P": "6", "J": "6?", "V": "6!"},  {"D": "7", "W": "7?", "G": "7!"},  {"E": "8", "K": "8?", "Z": "8!"},  {"L": "9", "C": "9?"}]
encryption2_backup = [null, "B", "M", "L", "P", "A", "E", "S", "V", "O"]

encryption1 = [null, {"M": "1", "B": "1?", "Y": "1!"},  {"A": "2", "N": "2?", "T": "2!"},  {"O": "3", "H": "3?", "U": "3!"},  {"I": "4", "F": "4?", "S": "4!"},  {"Q": "5", "X": "5?", "R": "5!"},  {"P": "6", "J": "6?", "V": "6!"},  {"D": "7", "W": "7?", "G": "7!"},  {"E": "8", "K": "8?", "Z": "8!"},  {"L": "9", "C": "9?"}]
encryption2 = [null, "B", "M", "L", "P", "A", "E", "S", "V", "O"]

ignore = [" ", ".", ",", "-", "\"", "&", "/", "(", ")", "=", "<", ">", ":", ";", "_", "*", "+"]

function open_file(file_to_open, ask) {
    try {
        if (fs.existsSync(file_to_open)) {
            if (ask) {
                rl.question("Encryption file found. Do you want to use the encryption from the file? (Y / N)\n", answer => {
                    if (answer.toUpperCase() === "Y") {
                        fs.readFile(file_to_open, (err, data) => {
                            completeData = data.toString().split("\n")
                            if (completeData[0].startsWith("e:")) {
                                completeData[0] = completeData[0].slice(2)
                                if (completeData[1].startsWith("e:")) {
                                    completeData[1] = completeData[1].slice(2)
                                    if (completeData[0] == {}) encryption1 = encryption1_backup
                                    if (completeData[1] == {}) encryption2 = encryption2_backup
                                    else if (completeData[0] != {}) encryption1 = JSON.parse(completeData[0])
                                    else if (completeData[1] != {}) encryption2 = JSON.parse(completeData[1])
                                    ask_letters()
                                } else {
                                    console.error("Missing encryption signature.");
                                    open_file(file_to_open, true)
                                }
                            } else {
                                console.error("Missing encryption signature.");
                                open_file(file_to_open, true)
                            }
                        })
                    } else if (answer.toUpperCase() === "N") {
                        ask_standard()
                    } else {open_file(file_to_open, true)}
                })
            } else {
                fs.readFile(file_to_open, (err, data) => {
                    completeData = data.toString().split("\n")
                    if (completeData[0].startsWith("e:")) {
                        completeData[0] = completeData[0].slice(2)
                        if (completeData[1].startsWith("e:")) {
                            completeData[1] = completeData[1].slice(2)
                            if (completeData[0] == {}) encryption1 = encryption1_backup
                            if (completeData[1] == {}) encryption2 = encryption2_backup
                            else if (completeData[0] != {}) encryption1 = JSON.parse(completeData[0])
                            else if (completeData[1] != {}) encryption2 = JSON.parse(completeData[1])
                            ask_letters()
                        } else {
                            console.error("Missing encryption signature.");
                            exit()
                        }
                    } else {
                        console.error("Missing encryption signature.");
                        exit()
                    }
                })
            }
        } else {
            ask_standard()
        }
    } catch (err) {
        console.error(`Error found!\n${err}\n`)
    }
}

function ask_standard() {
    rl.question("Do you want to use the standard encryption values? (Y / N)\n", answer => {
        if (answer.toUpperCase() === "Y") {
            open_file("../Presets/Default/e-default-preset.txt", false)
            ask_letters()
        } else if (answer.toUpperCase() === "N") {
            define_encryption1()
        } else {
            ask_standard()
        }
    })
}
function define_encryption1() {
    rl.question("Define encryption1. (Type \"skip\" to use the default)\n", string => {
        if (string.toLowerCase() != "skip") {
            try {
                if (string.startsWith("e:")) {
                    encryption1 = JSON.parse(string.slice(2))
                    define_encryption2()
                } else {
                    console.error("Invalid encryption code");
                    define_encryption1()
                }
            } catch (error) {
                console.error(`Error found!\n${error}\n`)
                define_encryption1()
            }
        } else {
            encryption1 = encryption1_backup
            define_encryption2()
        }
    })
}
function define_encryption2() {
    rl.question("Define encryption2. (Type \"skip\" to use the default)\n", string => {
        if (string.toLowerCase() != "skip") {
            try {
                if (string.startsWith("e:")) {
                    encryption2 = JSON.parse(string.slice(2))
                    ask_letters()
                } else {
                    console.error("Invalid encryption code");
                    define_encryption1()
                }
            } catch (error) {
                console.error(`Error found!\n${error}\n`)
                define_encryption2()
            }
        } else {
            encryption2 = encryption2_backup
            ask_letters()
        }
    })
}

function ask_letters() {
    rl.question("What do you want to encrypt?\n", string => {
        console.log("\nResult: " + encrypt2(encrypt1(string)) + "\n\n");
        ask_letters()
    })
}

function encrypt1(str) {
    let value = "";
    for (const s of str) {
        ignoring = false;
        for (const i of ignore) {
            if (i == s) {
                value += s;
                ignoring = true;
                break
            }
        }
        if (!ignoring) {
            for (let i = 1; i <= 9; i++) {
                for (v in encryption1[i]) {
                    if (s == v) {
                        value += encryption1[i][v]
                        break
                    } 
                    else if (s == v.toLowerCase()) {
                        if (encryption1[i][v].charAt(1) == "?" || encryption1[i][v].charAt(1) == "!") {
                            value += `${encryption1[i][v].charAt(0)}#${encryption1[i][v].charAt(1)}`
                            break
                        } else {
                            value += `${encryption1[i][v]}#`
                            break
                        }
                    }
                }
            }
        }
    }
    return value;
}
function encrypt2(str, EorD) {
    let value = "";
    let pos = 0;
    if (EorD == "e") {
        for (const s of str) {
            ignoring = false;
            for (const i of ignore) {
                if (i == s) {
                    value += s;
                    ignoring = true;
                    break
                }
            }
            if (!ignoring) {
                if (s === "?" || s === "!" || s === "_" || s === " ") {
                    value += s;
                }
                else if (str[pos+1] == "#") {
                    if (s == "1") value += "b"
                    else value += encryption2[Number(s)].toLowerCase();
                }
                else if (s === "#") value += "";
                else if (s === s.toUpperCase()) {
                    if (s == "1") value += "B"
                    else value += encryption2[Number(s)];
                }
            }
            pos++;
        }
    } else if (EorD == "d") {
        for (const s of val) {
            ignoring = false;
            for (const i of ignore) {
                if (i == s) {
                    value += s;
                    ignoring = true;
                    break
                }
            }
            if (!ignoring) {
                if (val[pos+1] == "#") {
                    if (val[pos+2] == "?") value += encryption2_lc[s][1];
                    else if (val[pos+2] == "!") value += encryption2_lc[s][2];
                    else value += encryption2_lc[s][0];
                }
                else if (s == "?" || s == "!" || s == "#") value += "";
                else if (val[pos+1] == "!") value += encryption2[s][2];
                else if (val[pos+1] == "?") value += encryption2[s][1];
                else value += encryption2[s][0];
            }
            pos++;
        }
    }
    return value;
}

open_file(presetFile, true)