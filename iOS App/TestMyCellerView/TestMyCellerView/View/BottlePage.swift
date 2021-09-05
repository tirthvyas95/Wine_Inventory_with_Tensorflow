//
//  BottlePage.swift
//  TestMyCellerView
//
//  Created by Tirth Vyas on 2020-12-09.
//

import SwiftUI

struct BottlePage: View {
    
    var body: some View {
        VStack(spacing: 20) {
            ZStack {
                Rectangle()
                    .fill(Color.black)
                    .frame(width: 260, height:40, alignment: .center)
                Text("Bottle Description")
                    .foregroundColor(.white)
                    .font(.title)
                    .fontWeight(.heavy)
            }.padding(.bottom, 10)
            HStack(alignment: .top) {
                Text("Stellenbosch Cabernet Sauvignon")
            }
            VStack {
                Image("SWine")
                    .resizable()
                    .scaledToFit()
                    .frame(width: 500, height: 500, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
                    .border(/*@START_MENU_TOKEN@*/Color.black/*@END_MENU_TOKEN@*/, width: /*@START_MENU_TOKEN@*/1/*@END_MENU_TOKEN@*/)
                Text("Rate This Wine>")
                    .foregroundColor(/*@START_MENU_TOKEN@*/.blue/*@END_MENU_TOKEN@*/)
                    .padding(.trailing, 360)
                    .padding(.bottom, /*@START_MENU_TOKEN@*/10/*@END_MENU_TOKEN@*/)
                HStack(alignment: .firstTextBaseline) {
                    VStack(alignment: .center) {
                        Text("Ordered")
                            .foregroundColor(.black)
                        Text("0")
                    }.padding(.trailing, 30)
                    VStack(alignment: .center) {
                        Text("In Stock")
                            .foregroundColor(.black)
                        Text("2")
                    }.padding(.trailing, 30)
                    VStack(alignment: .center) {
                        Text("Consumed")
                            .foregroundColor(.black)
                        Text("4")
                    }
                }
            }.padding(.bottom, 20)
            HStack {
                Text("Add to Celler")
                    .frame(width: 100, height: /*@START_MENU_TOKEN@*/100/*@END_MENU_TOKEN@*/, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
                    .padding(.trailing, 50)
                    .foregroundColor(/*@START_MENU_TOKEN@*/.blue/*@END_MENU_TOKEN@*/)
                Text("Add to Wishlist")
                    .frame(width: 150, height: /*@START_MENU_TOKEN@*/100/*@END_MENU_TOKEN@*/, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
                    .foregroundColor(/*@START_MENU_TOKEN@*/.blue/*@END_MENU_TOKEN@*/)
                    .padding(.trailing, 40)
                Text("Where to Buy")
                    .frame(width: 140, height: /*@START_MENU_TOKEN@*/100/*@END_MENU_TOKEN@*/, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
                    .foregroundColor(/*@START_MENU_TOKEN@*/.blue/*@END_MENU_TOKEN@*/)
            }
            ZStack {
                Rectangle()
                    .fill(Color.red)
                    .frame(width: 200, height:40, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
                Text("Drink or Remove")
                    .foregroundColor(.white)
                    .font(.headline)
                    .fontWeight(.heavy)
            }
        }
    }
}

struct BottlePage_Previews: PreviewProvider {
    static var previews: some View {
        BottlePage()
            .previewDevice(PreviewDevice(rawValue: "iPad Pro (9.7-inch)"))
    }
}
