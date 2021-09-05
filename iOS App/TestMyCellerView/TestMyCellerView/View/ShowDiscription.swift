//
//  ShowDiscription.swift
//  TestMyCellerView
//
//  Created by Tirth Vyas on 2021-03-19.
//

import SwiftUI

struct ShowDiscription: View {
    @EnvironmentObject var testdata1: testdata
    @State var count = 0
    @State var index = 0
    
    func check() {
        index = testdata1.savecount.firstIndex(of: testdata1.slotnum) ?? 0
    }
    var body: some View {
        VStack {
            ZStack {
                Rectangle()
                    .fill(Color.black)
                    .frame(width: 245, height:40, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
            Text("Bottle Discription")
                .foregroundColor(.white)
                .font(.title)
                .fontWeight(.bold)
            }
            Section {
                HStack {
                    Text("Bottle Name:")
//            guard (testdata1.bottlename.count >= count) else {
                    Text(testdata1.savecount.contains(testdata1.slotnum) ? testdata1.bottlename[testdata1.bottlename.index(testdata1.bottlename.startIndex, offsetBy: index)] : "nil")
//                    Text(testdata1.bottlename[testdata1.bottlename.index(testdata1.bottlename.startIndex, offsetBy: index)])
//                Text("ggg")
//            }
                }.onAppear(perform: {
                    check()
                })
                    //Text("Bottle Name:")
//                    Text(testdata1.bottlename[testdata1.bottlename.index(testdata1.bottlename.startIndex, offsetBy: count)])
            }
            //dataArray[dataArray.index(dataArray.startIndex, offsetBy: val)]
            //}
            Section {
                HStack {
                    Text("Vintage:")
//                    Text(testdata1.vintage[testdata1.vintage.index(testdata1.vintage.startIndex, offsetBy: index)])
                    Text(testdata1.savecount.contains(testdata1.slotnum) ? testdata1.vintage[testdata1.vintage.index(testdata1.vintage.startIndex, offsetBy: index)] : "nil")
                }
//            //dataArray[dataArray.index(dataArray.startIndex, offsetBy: val)]
            }
            Section {
                HStack {
                    Text("Type:")
                    Text(testdata1.savecount.contains(testdata1.slotnum) ? testdata1.type[testdata1.type.index(testdata1.type.startIndex, offsetBy: index)] : "nil")
//                    Text(testdata1.type[testdata1.type.index(testdata1.type.startIndex, offsetBy: index)])
                }
//            //dataArray[dataArray.index(dataArray.startIndex, offsetBy: val)]
            }
            Section {
                HStack {
                    Text("Producer:")
                    Text(testdata1.savecount.contains(testdata1.slotnum) ? testdata1.producer[testdata1.producer.index(testdata1.producer.startIndex, offsetBy: index)] : "nil")
//                   Text(testdata1.producer[testdata1.producer.index(testdata1.producer.startIndex, offsetBy: index)])
                }
//            //dataArray[dataArray.index(dataArray.startIndex, offsetBy: val)]
            }
            Section {
                HStack {
                    Text("Country:")
                    Text(testdata1.savecount.contains(testdata1.slotnum) ? testdata1.country[testdata1.country.index(testdata1.country.startIndex, offsetBy: index)] : "nil")
//                    Text(testdata1.country[testdata1.country.index(testdata1.country.startIndex, offsetBy: index)])
                }
//            //dataArray[dataArray.index(dataArray.startIndex, offsetBy: val)]
            }
            Section {
                HStack {
                    Text("Price:")
                    Text(testdata1.savecount.contains(testdata1.slotnum) ? testdata1.price[testdata1.price.index(testdata1.price.startIndex, offsetBy: index)] : "nil")
//                   Text(testdata1.price[testdata1.price.index(testdata1.price.startIndex, offsetBy: index)])
                }
//            //dataArray[dataArray.index(dataArray.startIndex, offsetBy: val)]
            }
        }.onAppear(perform: {
            for save in testdata1.savecount {
                if save == testdata1.slotnum {
                    count = index
                    break
                }
                index += 1
            }
        })
    }
}

struct ShowDiscription_Previews: PreviewProvider {
    static var previews: some View {
        ShowDiscription()
    }
}
