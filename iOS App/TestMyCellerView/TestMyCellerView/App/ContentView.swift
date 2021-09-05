//
//  ContentView.swift
//  TestMyCellerView
//
//  Created by Tirth Vyas on 2020-12-02.
//

import SwiftUI
import Foundation

struct ContentView: View {
    
    var body: some View {
        VStack(alignment: .leading) {
            Text("NAME")
                .font(.headline)
        }
    }
    
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
            .previewDevice(PreviewDevice(rawValue: "iPad Pro (9.7-inch)"))
            .scaledToFit()
    }
}
