//
//  BottleDiscription.swift
//  TestMyCellerView
//
//  Created by Tirth Vyas on 2021-02-02.
//

import SwiftUI

struct BottleDiscription: View {
    
    @EnvironmentObject var testdata1: testdata
    
    @State var bottlenameph = ""
    @State var vintageph = ""
    @State var typeph = ""
    @State var producerph = ""
    @State var countryph = ""
    @State var priceph = ""
    
    @State private var isShowingCel = false
    
    func addata1() {
        guard bottlenameph.count > 0 else {
            return
        }
        
        testdata1.bottlename.append(bottlenameph)
    }
    
   func addata2() {
        guard vintageph.count > 0 else {
            return
        }
        
        testdata1.vintage.append(vintageph)
    }
    
    func addata3() {
        guard typeph.count > 0 else {
            return
        }
        
        testdata1.type.append(typeph)
    }
    
    func addata4() {
        guard producerph.count > 0 else {
            return
        }
        
        testdata1.producer.append(producerph)
    }
    
    func addata5() {
        guard countryph.count > 0 else {
            return
        }
        
        testdata1.country.append(countryph)
    }
    
    func addata6() {
        guard priceph.count > 0 else {
            return
        }
        
        testdata1.price.append(priceph)
    }
    
    var body: some View {
        NavigationView {
            VStack() {
                NavigationLink(destination: MyCellerView(), isActive: $isShowingCel) {
                    EmptyView()
                }
                ZStack {
                    Rectangle()
                        .fill(Color.black)
                        .frame(width: 245, height:40, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
                    Text("Add a Discription")
                        .foregroundColor(.white)
                        .font(.title)
                        .fontWeight(.heavy)
                }.padding(.bottom, 70)
            
                TextField("Bottle Name", text: $bottlenameph, onCommit: addata1)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                    .frame(width: 300, height:50, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
                //dataArray[dataArray.index(dataArray.startIndex, offsetBy: val)]
                
                TextField("Vintage", text: $vintageph, onCommit: addata2)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                    .frame(width: 300, height:50, alignment: .center)
                
                TextField("Type", text: $typeph, onCommit: addata3)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                    .frame(width: 300, height:50, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
                
                TextField("Producer", text: $producerph, onCommit: addata4)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                    .frame(width: 300, height:50, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
                
                TextField("Country", text: $countryph, onCommit: addata5)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                    .frame(width: 300, height:50, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
                
                TextField("Price", text: $priceph, onCommit: addata6)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                    .frame(width: 300, height:50, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
                    .padding(.bottom, 50)
                
                //SaveButtonView()
                Button(action: {
                    testdata1.savecount.append(testdata1.slotnum)
                }) {
                    HStack(spacing: 8) {
                        Text("Save")
                        
                        Image(systemName: "arrow.down.doc")
                            .imageScale(.large)
                    }
                    .padding(.horizontal, 16)
                    .padding(.vertical, 10)
                    .background(Capsule().strokeBorder(Color.black, lineWidth: 1.25))
                } //: BUTTON
                .accentColor(Color.black)
            }
        }
    }
}

//struct BottleDiscription_Previews: PreviewProvider {
  //  static var previews: some View {
    //    BottleDiscription(data: DataModel.Type)
      //      .previewDevice(PreviewDevice(rawValue: "iPad Pro (9.7-inch)"))
        //    .scaledToFit()
    //}
//}
