//
//  SmallSearch.swift
//  TestMyCellerView
//
//  Created by Tirth Vyas on 2020-12-09.
//

import SwiftUI

struct SmallSearch: View {
    var body: some View {
        Button(action: {
            print("Small Search")
        }) {
            Image(systemName: "arrow.right.circle")
                .imageScale(.large)
        } //: BUTTON
        .accentColor(Color.black)
    }
}

struct SmallSearch_Previews: PreviewProvider {
    static var previews: some View {
        SmallSearch().previewLayout(.sizeThatFits)
    }
}
