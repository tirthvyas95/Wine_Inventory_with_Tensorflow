//
//  SpecialButton.swift
//  TestMyCellerView
//
//  Created by Tirth Vyas on 2021-01-20.
//

import SwiftUI

struct SpecialButton: View {
    
    var buttonColor = Color("ColorRed")
    var body: some View {
        //Text(/*@START_MENU_TOKEN@*/"Hello, World!"/*@END_MENU_TOKEN@*/)
        Rectangle()
            .fill(buttonColor)
            .frame(width: 20, height: 20, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
            .rotationEffect(.degrees(45))
        
    }
}

struct SpecialButton_Previews: PreviewProvider {
    static var previews: some View {
        SpecialButton()
    }
}
