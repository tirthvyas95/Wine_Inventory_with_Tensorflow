//
//  SearchButtonView.swift
//  TestMyCellerView
//
//  Created by Tirth Vyas on 2020-12-02.
//

import SwiftUI

struct SearchButtonView: View {
    
    
    var body: some View {
        //var count = Int
        
        Button(action: {
        }) {
            HStack(spacing: 8) {
                Text("Search")
                
                Image(systemName: "arrow.right.circle")
                    .imageScale(.large)
            }
            .padding(.horizontal, 16)
            .padding(.vertical, 10)
            .background(Capsule().strokeBorder(Color.black, lineWidth: 1.25))
        } //: BUTTON
        .accentColor(Color.black)
    }
}

struct SearchButtonView_Previews: PreviewProvider {
    static var previews: some View {
        SearchButtonView()
            .previewLayout(.sizeThatFits)
    }
}
