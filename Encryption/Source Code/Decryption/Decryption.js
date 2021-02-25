const fs = require('fs');
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const presetFile = "../Presets/decryption.txt"

encryption1_backup = {"B": "1", "M": "2", "L": "3", "P": "4", "A": "5", "E": "6", "S": "7", "V": "8", "O": "9"}
encryption2_backup = {"1": ["M", "B", "Y"], "2": ["A", "N", "T"], "3": ["O", "H", "U"], "4": ["I", "F", "S"], "5": ["Q", "X", "R"], "6": ["P", "J", "V"], "7": ["D", "W", "G"], "8": ["E", "K", "Z"], "9": ["L", "C"]};

encryption1_lc_backup = {"b": "1", "m": "2", "l": "3", "p": "4", "a": "5", "e": "6", "s": "7", "v": "8", "o": "9"}
encryption2_lc_backup = {"1": ["m", "b", "y"], "2": ["a", "n", "t"], "3": ["o", "h", "u"], "4": ["i", "f", "s"], "5": ["q", "x", "r"], "6": ["p", "j", "v"], "7": ["d", "w", "g"], "8": ["e", "k", "z"], "9": ["l", "c"]};

encryption1 = {"B": "1", "M": "2", "L": "3", "P": "4", "A": "5", "E": "6", "S": "7", "V": "8", "O": "9"}
encryption2 = {"1": ["M", "B", "Y"], "2": ["A", "N", "T"], "3": ["O", "H", "U"], "4": ["I", "F", "S"], "5": ["Q", "X", "R"], "6": ["P", "J", "V"], "7": ["D", "W", "G"], "8": ["E", "K", "Z"], "9": ["L", "C"]};

encryption1_lc = {"b": "1", "m": "2", "l": "3", "p": "4", "a": "5", "e": "6", "s": "7", "v": "8", "o": "9"}
encryption2_lc = {"1": ["m", "b", "y"], "2": ["a", "n", "t"], "3": ["o", "h", "u"], "4": ["i", "f", "s"], "5": ["q", "x", "r"], "6": ["p", "j", "v"], "7": ["d", "w", "g"], "8": ["e", "k", "z"], "9": ["l", "c"]};

ignore = [" ", ".", ",", "-", "\"", "&", "/", "(", ")", "=", "<", ">", ":", ";", "_", "*", "+"]

function open_file(file_to_open, ask) {
    try {
        if (fs.existsSync(file_to_open)) {
            if (ask) {
                rl.question("Decryption file found. Do you want to use the decryption from the file? (Y / N)\n", answer => {
                    if (answer.toUpperCase() === "Y") {
                        fs.readFile(file_to_open, (err, data) => {
                            completeData = data.toString().split("\n")
                            if (completeData[0].startsWith("d:")) {
                                completeData[0] = completeData[0].slice(2)
                                if (completeData[1].startsWith("d:")) {
                                    completeData[1] = completeData[1].slice(2)
                                    if (completeData[0] == {}) encryption2 = encryption1_backup
                                    if (completeData[1] == {}) encryption1 = encryption2_backup
                                    else if (completeData[0] != {}) {encryption2 = JSON.parse(completeData[0]); encryption2_lc = JSON.parse(completeData[0].toLowerCase());}
                                    else if (completeData[1] != {}) {encryption1 = JSON.parse(completeData[1]); encryption1_lc = JSON.parse(completeData[1].toLowerCase());}
                                    ask_letters()
                                } else {
                                    console.error("Missing decryption signature.");
                                    open_file(file_to_open, true)
                                }
                            } else {
                                console.error("Missing decryption signature.");
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
                    if (completeData[0].startsWith("d:")) {
                        completeData[0] = completeData[0].slice(2)
                        if (completeData[1].startsWith("d:")) {
                            completeData[1] = completeData[1].slice(2)
                            if (completeData[0] == {}) encryption2 = encryption1_backup
                            if (completeData[1] == {}) encryption1 = encryption2_backup
                            else if (completeData[0] != {}) {encryption2 = JSON.parse(completeData[0]); encryption2_lc = JSON.parse(completeData[0].toLowerCase());}
                            else if (completeData[1] != {}) {encryption1 = JSON.parse(completeData[1]); encryption1_lc = JSON.parse(completeData[1].toLowerCase());}
                            ask_letters()
                        } else {
                            console.error("Missing decryption signature.");
                            exit()
                        }
                    } else {
                        console.error("Missing decryption signature.");
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
        if (answer.toLowerCase() == "y") {
            open_file("../Presets/Default/d-default-preset.txt", false)
            ask_letters()
        } else if (answer.toLowerCase() == "n") {
            define_encryption1()
        } else {
            ask_standard()
        }
    })
}
function define_encryption1() {
    rl.question("Define decryption1. (Type \"skip\" to use the default)\n", string => {
        if (string.toLowerCase() != "skip") {
            try {
                if (string.startsWith("d:")) {
                    encryption2 = JSON.parse(string.slice(2))
                    encryption2_lc = JSON.parse(string.slice(2).toLowerCase())
                    define_encryption2()
                } else {
                    console.error("Invalid decryption code");
                    define_encryption2()
                }
            } catch (error) {
                console.error(`Error found!\n${error}\n`)
                define_encryption1()
            }
        } else {
            encryption2 = encryption2_backup
            encryption2_lc = encryption2_lc_backup
            define_encryption2()
        }
    })
}
function define_encryption2() {
    rl.question("Define decryption2. (Type \"skip\" to use the default)\n", string => {
        if (string.toLowerCase() != "skip") {
            try {
                if (string.startsWith("d:")) {
                    encryption1 = JSON.parse(string.slice(2))
                    encryption1_lc = JSON.parse(string.slice(2).toLowerCase())
                    ask_letters()
                } else {
                    console.error("Invalid decryption code");
                    define_encryption2()
                }
            } catch (error) {
                console.error(`Error found!\n${error}\n`)
                define_encryption2()
            }
        } else {
            encryption1 = encryption1_backup
            encryption1_lc = encryption1_lc_backup
            ask_letters()
        }
    })
}

function ask_letters() {
    rl.question("What do you want to decrypt?\n", string => {
        console.log("\nResult: " + decrypt2(decrypt1(string)) + "\n\n");
        ask_letters()
    })
}

function decrypt1(str) {
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
            if (s === "?" || s === "!" || s === "_" || s === " ") value += s;
            else if (s == s.toUpperCase()) {
                value += encryption1[s.toUpperCase()];
            } else if (s == s.toLowerCase()) {
                value += encryption1_lc[s.toLowerCase()];
                value += "#"
            }
        }
    }
    return value;
}
function decrypt2(val) {
    let value = "";
    let pos = 0
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
    return value;
}

open_file(presetFile, true)