//
//  MyCellerView.swift
//  TestMyCellerView
//
//  Created by Tirth Vyas on 2020-12-02.
//

import SwiftUI

struct MyCellerView2: View {
    @State var bybottle: String = ""
    @State var row: String = ""
    @State var column: String = ""
    
    
    var body: some View {
        //@State var results = [posts]()
        
        VStack(spacing: 20) {
            // FRUIT: TITLE
            //Text("MY CELLER")
            //    .foregroundColor(Color.white)
            //    .font(.title)
            //    .fontWeight(.heavy)
            //    .shadow(color: Color(red: 0, green: 0, blue: 0, opacity: 0.15), radius: 2, x: 2, y: 2)
            //    .background(RoundedRectangle(cornerRadius: 10))
            ZStack {
                Rectangle()
                    .fill(Color.black)
                    .frame(width: 150, height:40, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
                Text("My Celler")
                    .foregroundColor(.white)
                    .font(.title)
                    .fontWeight(.heavy)
            }
            VStack(alignment: .center) {
                HStack {
                    TextField("By Bottle", text: $bybottle)
                        .textFieldStyle(RoundedBorderTextFieldStyle())
                        .frame(width: 200, height:50, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
                    SmallSearch()
                }
            }
            // FRUIT: IMAGE
            //Image("celler")
            //    .resizable()
            //    .scaledToFit()
            VStack(alignment: .center)
            {
                HStack(alignment: .center)
                {
                    Text("1").bold().padding(5)
                    Text("2").bold().padding(5)
                    Text("3").bold().padding(5)
                    Text("4").bold().padding(5)
                    Text("5").bold().padding(5)
                    Text("6").bold().padding(5)
                    Text("7").bold().padding(5)
                    Text("8").bold().padding(5)
                }
                HStack(alignment: .center)
                {
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                }
                HStack(alignment: .center)
                {
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                }
                HStack(alignment: .center)
                {
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                }
                HStack(alignment: .center)
                {
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                }
                HStack(alignment: .center)
                {
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                }
                HStack(alignment: .center)
                {
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                }
                HStack(alignment: .center)
                {
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                }
                HStack(alignment: .center)
                {
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                }
            HStack(alignment: .center)
            {
                SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                    {
                    print("1")
                    }
                SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                    {
                    print("1")
                    }
                SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                    {
                    print("1")
                    }
                SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                    {
                    print("1")
                    }
                SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                    {
                    print("1")
                    }
                SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                    {
                    print("1")
                    }
                SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                    {
                    print("1")
                    }
            }
            }
                
            VStack(alignment: .center)
            {
                HStack(alignment: .center)
                {
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                }
                HStack(alignment: .center)
                {
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                }
                HStack(alignment: .center)
                {
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                }
                HStack(alignment: .center)
                {
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                }
                HStack(alignment: .center)
                {
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                }
                HStack(alignment: .center)
                {
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                }
                HStack(alignment: .center)
                {
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                }
                HStack(alignment: .center)
                {
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                }
                HStack(alignment: .center)
                {
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                }
                HStack(alignment: .center)
                {
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                }
                HStack(alignment: .center)
                {
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorGreen")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                    SpecialButton(buttonColor: Color("ColorRed")).onTapGesture
                        {
                        print("1")
                        }
                }
            }
            
            Text("Search by Row and Column")
            HStack(alignment: .center) {
                Text("Row")
                TextField("",text: $row).frame(width: 40, height: 20, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
                    .border(Color.black)
                Text("Column")
                TextField("",text: $column).frame(width: 40, height: 20, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
                    .border(/*@START_MENU_TOKEN@*/Color.black/*@END_MENU_TOKEN@*/)
            }.frame(width: 300, height: 20, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
            SearchButtonView()
        }//.frame(width: 1536, height: 2048, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)//: VSTACK
        }
}

//MARK: - PREVIEW

struct MyCellerView_Previews: PreviewProvider {
    static var previews: some View {
        MyCellerView()
            .previewDevice(PreviewDevice(rawValue: "iPad Pro (9.7-inch)"))
            .scaledToFit()
    }
}

