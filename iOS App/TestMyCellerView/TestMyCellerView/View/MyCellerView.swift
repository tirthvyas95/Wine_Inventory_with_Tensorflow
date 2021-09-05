//
//  MyCellerView.swift
//  TestMyCellerView
//
//  Created by Tirth Vyas on 2020-12-02.
//

import SwiftUI
import Foundation

class testdata: ObservableObject {
    @Published var bottlename = [String]()
    @Published var vintage = [String]()
    @Published var type = [String]()
    @Published var producer = [String]()
    @Published var country = [String]()
    @Published var price = [String]()
    @Published var discount = [Int]()
    @Published var savecount = [Int]()
    @Published var slotstate = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    @Published var slotnum = Int()
}

struct MyCellerView: View {
    
    @EnvironmentObject var testdata1: testdata
    
    @State var bybottle: String = ""
    @State var row: String = ""
    @State var column: String = ""
    
    @State var test = ""
    @State public var x = Int()
    @State public var count = Int()
    
    @State private var isShowingDis = false
    @State private var isShowingDis2 = false
    
    
    //func valinc(val: Int) -> Int {
      //  x = 16
        //count = count + 1
        //print(count)
        //print(x)
        //return 16
    //}
    
    
    func loadData() {
        guard let url = URL(string: "http://192.168.2.115:3000/posts") else {
                print("Invalid URL")
                return
            }
            
        let request = URLRequest(url: url)
            
        URLSession.shared.dataTask(with: request) {
            data, response, error in
            guard let data = data else { return }
                
            test = String(data: data, encoding: .utf8) ?? "X"
            //for letter in test {
              //  dataArray[dataArray.index(dataArray.startIndex, offsetBy: count)] = letter
                //count = count + 1
            //}
            //print(test)
            //print(test[test.index(test.startIndex, offsetBy: 82)])
            
            
            
            
            //dataArray[dataArray.index(dataArray.startIndex, offsetBy: 0)] = test[test.index(test.startIndex, offsetBy: 82)]
            
            //for letter in test {
              //  print("\(count) = \(letter)")
                //count = count + 1
            //}
        }.resume()
    }
    
    func loadcolor(val: Int, val2: Int) -> String {
        if testdata1.savecount.contains(val2) {
            return "ColorGreen"
        }
        else {
            let dataArray = Array(test)
            //print(testdata1.slotstate.count)
    //        guard (testdata1.slotstate.count >= val2) else {
    //            return "ColorGreen"
    //        }
                if dataArray.indices.contains(val) {
                    if dataArray[dataArray.index(dataArray.startIndex, offsetBy: val)] == "X" {
    //                    testdata1.slotstate.remove(at: val2)
    //                    testdata1.slotstate.insert(1, at: val2)
                        return "ColorYellow"
                    }
                    else {
    //                    testdata1.slotstate.remove(at: val2)
    //                    testdata1.slotstate.insert(0, at: val2)
                        return "ColorRed"
                    }
                }
                else {
    //                guard (testdata1.slotstate.count >= val2) else {
    //                    return "ColorGreen"
    //                }
                    //testdata1.slotstate[val2] = 2
    //                testdata1.slotstate.remove(at: val2)
    //                testdata1.slotstate.insert(2, at: val2)
                    return "ColorGreen"
                }
        }
    }
    func slotstatefun(val: String, val2: Int) {
        if testdata1.savecount.contains(val2) {
            testdata1.slotnum = val2
            self.isShowingDis2 = true
        }
        else {
            if (val == "ColorYellow") {
                testdata1.slotstate.remove(at: val2)
                testdata1.slotstate.insert(1, at: val2)
                self.isShowingDis = true
                testdata1.slotnum = val2
            }
            if (val == "ColorGreen") {
                testdata1.slotstate.remove(at: val2)
                testdata1.slotstate.insert(2, at: val2)
            }
            if (val == "ColorRed") {
                testdata1.slotstate.remove(at: val2)
                testdata1.slotstate.insert(0, at: val2)
            }
        //print(testdata1.slotstate[val2])
        }
    }
    
    var body: some View {
        NavigationView() {
        //var x = 16
        //@State var results = [posts]()
        VStack(spacing: 20) {
            NavigationLink(destination: BottleDiscription(), isActive: $isShowingDis) {
                EmptyView()
            }
            NavigationLink(destination: ShowDiscription(), isActive: $isShowingDis2) {
                EmptyView()
            }
            // FRUIT: TITLE
            //Text("MY CELLER")
            //    .foregroundColor(Color.white)
            //    .font(.title)
            //    .fontWeight(.heavy)
            //    .shadow(color: Color(red: 0, green: 0, blue: 0, opacity: 0.15), radius: 2, x: 2, y: 2)
            //    .background(RoundedRectangle(cornerRadius: 10))
            //ZStack {
              //  Rectangle()
                //    .fill(Color.black)
                  //  .frame(width: 150, height:40, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
                //Text("My Celler")
                  //  .foregroundColor(.white)
                    //.font(.title)
                    //.fontWeight(.heavy)
            //}
            //VStack(alignment: .center) {
              //  HStack {
                //    TextField("By Bottle", text: $bybottle)
                  //      .textFieldStyle(RoundedBorderTextFieldStyle())
                    //    .frame(width: 200, height:50, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
                    //SmallSearch()
                //}
            //}
            VStack(alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/, spacing: /*@START_MENU_TOKEN@*/nil/*@END_MENU_TOKEN@*/, content: {
                
//                HStack(alignment: .center, spacing: 25) {
//                    Text("1")
//                    Text("2")
//                    Text("3")
//                    Text("4")
//                    Text("5")
//                    Text("6")
//                    Text("7")
//                }
                VStack(alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/, spacing: /*@START_MENU_TOKEN@*/nil/*@END_MENU_TOKEN@*/, content: {
                    HStack(alignment: .center, spacing: 25)
                    {
                        SpecialButton(buttonColor: Color(loadcolor(val: 16, val2: 1))).onTapGesture
                            {
                            slotstatefun(val: loadcolor(val: 16, val2: 1), val2: 1)
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 38, val2: 2))).onTapGesture
                            {
                            slotstatefun(val: loadcolor(val: 38, val2: 2), val2: 2)
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 60, val2: 3))).onTapGesture
                            {
                            slotstatefun(val: loadcolor(val: 60, val2: 3), val2: 3)
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 82, val2: 4))).onTapGesture
                            {
                            slotstatefun(val: loadcolor(val: 82, val2: 1), val2: 4)
                            }
                    }.padding(3)
                    HStack(alignment: .center, spacing: 25)
                    {
                        SpecialButton(buttonColor: Color(loadcolor(val: 104, val2: 5))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 126, val2: 6))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 148, val2: 7))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 170, val2: 8))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 192, val2: 9))).onTapGesture
                            {
                            print("1")
                            }
                    }.padding(3)
                    
                    HStack(alignment: .center, spacing: 25)
                    {
                        SpecialButton(buttonColor: Color(loadcolor(val: 214, val2: 10))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 236, val2: 11))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 258, val2: 12))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 280, val2: 13))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 302, val2: 14))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 324, val2: 15))).onTapGesture
                            {
                            print("1")
                            }
                    }.padding(3)
                    
                    HStack(alignment: .center, spacing: 25)
                    {
                        SpecialButton(buttonColor: Color(loadcolor(val: 346, val2: 16))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 368, val2: 17))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 390, val2: 18))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 412, val2: 19))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 434, val2: 20))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 456, val2: 21))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 478, val2: 22))).onTapGesture
                            {
                            print("1")
                            }
                    }.padding(3)
                    
                    HStack(alignment: .center, spacing: 25)
                    {
                        SpecialButton(buttonColor: Color(loadcolor(val: 500, val2: 23))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 522, val2: 24))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 544, val2: 25))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 566, val2: 26))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 588, val2: 27))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 610, val2: 28))).onTapGesture
                            {
                            print("1")
                            }
                    }.padding(3)
                    
                    HStack(alignment: .center, spacing: 25)
                    {
                        SpecialButton(buttonColor: Color(loadcolor(val: 632, val2: 29))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 654, val2: 30))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 676, val2: 31))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 698, val2: 32))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 720, val2: 33))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 742, val2: 34))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 764, val2: 35))).onTapGesture
                            {
                            print("1")
                            }
                    }.padding(3)
                    
                    HStack(alignment: .center, spacing: 25)
                    {
                        SpecialButton(buttonColor: Color(loadcolor(val: 786, val2: 36))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 808, val2: 37))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 830, val2: 38))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 852, val2: 39))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 874, val2: 40))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 896, val2: 41))).onTapGesture
                            {
                            print("1")
                            }
                    }.padding(3)
                    
                    HStack(alignment: .center, spacing: 25)
                    {
                        SpecialButton(buttonColor: Color(loadcolor(val: 918, val2: 42))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 940, val2: 43))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 962, val2: 44))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 984, val2: 45))).onTapGesture
                            {
                            print("1")
                            }
//                        SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
//                            {
//                            print("1")
//                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1006, val2: 46))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1028, val2: 47))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1050, val2: 48))).onTapGesture
                            {
                            print("1")
                            }
                    }.padding(3)
                    
                    HStack(alignment: .center, spacing: 25)
                    {
                        SpecialButton(buttonColor: Color(loadcolor(val: 1072, val2: 49))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1094, val2: 50))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1116, val2: 51))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1138, val2: 52))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1160, val2: 53))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1182, val2: 54))).onTapGesture
                            {
                            print("1")
                            }
                    }.padding(3)
                    
                    HStack(alignment: .center, spacing: 25)
                    {
                        SpecialButton(buttonColor: Color(loadcolor(val: 1204, val2: 55))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1226, val2: 56))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1248, val2: 57))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1270, val2: 58))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1292, val2: 59))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1314, val2: 60))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1336, val2: 61))).onTapGesture
                            {
                            print("1")
                            }
                    }.padding(3)
                }).padding(.top, 20)
                VStack(alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/, spacing: /*@START_MENU_TOKEN@*/nil/*@END_MENU_TOKEN@*/, content: {
                    HStack(alignment: .center, spacing: 25)
                        {
                            SpecialButton(buttonColor: Color(loadcolor(val: 1358, val2: 62))).onTapGesture
                                {
                                print("1")
                                }
                            SpecialButton(buttonColor: Color(loadcolor(val: 1380, val2: 63))).onTapGesture
                                {
                                print("1")
                                }
                            SpecialButton(buttonColor: Color(loadcolor(val: 1402, val2: 64))).onTapGesture
                                {
                                print("1")
                                }
                            SpecialButton(buttonColor: Color(loadcolor(val: 1424, val2: 65))).onTapGesture
                                {
                                print("1")
                                }
                            SpecialButton(buttonColor: Color(loadcolor(val: 1446, val2: 66))).onTapGesture
                                {
                                print("1")
                                }
                            SpecialButton(buttonColor: Color(loadcolor(val: 1468, val2: 67))).onTapGesture
                                {
                                print("1")
                                }
                    }.padding(3)
                    
                    HStack(alignment: .center, spacing: 25)
                    {
                        SpecialButton(buttonColor: Color(loadcolor(val: 1490, val2: 68))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1512, val2: 69))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1534, val2: 70))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1556, val2: 71))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1578, val2: 72))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1600, val2: 73))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1622, val2: 74))).onTapGesture
                            {
                            print("1")
                            }
                    }.padding(3)
                    
                    HStack(alignment: .center, spacing: 25)
                    {
                        SpecialButton(buttonColor: Color(loadcolor(val: 1644, val2: 75))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1688, val2: 76))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1710, val2: 77))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1732, val2: 78))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1754, val2: 79))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1776, val2: 80))).onTapGesture
                            {
                            print("1")
                            }
                    }.padding(3)
                    
                    HStack(alignment: .center, spacing: 25)
                    {
                        SpecialButton(buttonColor: Color(loadcolor(val: 1798, val2: 81))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1820, val2: 82))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1842, val2: 83))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1864, val2: 84))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1886, val2: 85))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1908, val2: 86))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1930, val2: 87))).onTapGesture
                            {
                            print("1")
                            }
                    }.padding(3)
                    
                    HStack(alignment: .center, spacing: 25)
                    {
                        SpecialButton(buttonColor: Color(loadcolor(val: 1952, val2: 88))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1974, val2: 89))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 1996, val2: 90))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2018, val2: 91))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2040, val2: 92))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2062, val2: 93))).onTapGesture
                            {
                            print("1")
                            }
                    }.padding(3)
                    
                    HStack(alignment: .center, spacing: 25)
                    {
                        SpecialButton(buttonColor: Color(loadcolor(val: 2084, val2: 94))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2106, val2: 95))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2128, val2: 96))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2150, val2: 97))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2172, val2: 98))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2194, val2: 99))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2216, val2: 100))).onTapGesture
                            {
                            print("1")
                            }
                    }.padding(3)
                    
                    HStack(alignment: .center, spacing: 25)
                    {
                        SpecialButton(buttonColor: Color(loadcolor(val: 2238, val2: 101))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2260, val2: 102))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2282, val2: 103))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2304, val2: 104))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2326, val2: 105))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2348, val2: 106))).onTapGesture
                            {
                            print("1")
                            }
                    }.padding(3)
                    
                    HStack(alignment: .center, spacing: 25)
                    {
                        SpecialButton(buttonColor: Color(loadcolor(val: 2370, val2: 107))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2392, val2: 108))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2480, val2: 109))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2502, val2: 110))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2524, val2: 111))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2546, val2: 112))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2568, val2: 113))).onTapGesture
                            {
                            print("1")
                            }
                    }.padding(3)
                    
                    HStack(alignment: .center, spacing: 25)
                    {
                        SpecialButton(buttonColor: Color(loadcolor(val: 2590, val2: 114))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2612, val2: 115))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2634, val2: 116))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2656, val2: 117))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2678, val2: 118))).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color(loadcolor(val: 2700, val2: 119))).onTapGesture
                            {
                            print("1")
                            }
                    }.padding(3)
                    
                    HStack(alignment: .center, spacing: 25)
                    {
                        SpecialButton(buttonColor: Color("ColorYellow")).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color("ColorYellow")).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color("ColorYellow")).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color("ColorYellow")).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color("ColorYellow")).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color("ColorYellow")).onTapGesture
                            {
                            print("1")
                            }
                        SpecialButton(buttonColor: Color("ColorYellow")).onTapGesture
                            {
                            print("1")
                            }
                    }.padding(3)
                })
            }).onAppear(perform: loadData)
            .padding(.bottom, 30)
            
            // FRUIT: IMAGE
            //Image("celler")
            //    .resizable()
            //    .scaledToFit()
            
            //Text("Search by Row and Column")
//            HStack(alignment: .center) {
//                //Text("Row")
//                //TextField("",text: $row).frame(width: 40, height: 20, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
//                    //.border(Color.black)
//                //Text("Column")
//                TextField("Name or Slot",text: $column).frame(width: 190, height: 20, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
//                    .border(Color.black)
//                //TextField("By Bottle", text: $bybottle)
//            }.frame(width: 300, height: 20, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
//            SearchButtonView()
        }//.frame(width: 1536, height: 2048, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)//: VSTACK
        .navigationBarTitle("My Celler", displayMode: .inline)
        }
    }
}

//MARK: - PREVIEW

//struct MyCellerView_Previews: PreviewProvider {
//    static var previews: some View {
//        MyCellerView(testdata1: testdata)
//            .previewDevice(PreviewDevice(rawValue: "iPhone 12 Pro Max"))
//            .scaledToFit()
//    }
//}
