//
//  SaveButtonView.swift
//  TestMyCellerView
//
//  Created by Tirth Vyas on 2021-02-03.
//

import SwiftUI

struct SaveButtonView: View {
    var body: some View {
        Button(action: {
            print("Saved")
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

struct SaveButtonView_Previews: PreviewProvider {
    static var previews: some View {
        SaveButtonView()
            .previewLayout(.sizeThatFits)
    }
}
