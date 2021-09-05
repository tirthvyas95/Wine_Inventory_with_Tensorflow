//
//  TestMyCellerViewApp.swift
//  TestMyCellerView
//
//  Created by Tirth Vyas on 2020-12-02.
//

import SwiftUI

@main
struct TestMyCellerViewApp: App {
    
    @StateObject var testdata1 = testdata()
    
    var body: some Scene {
        WindowGroup {
            //ContentView()
            //MyCellerView()
            //BottlePage()
            //BottleDiscription().environmentObject(testdata1)
            //MyCellerView()
            //if myCeller {
              //  BottlePage()
            //}
            //else {
            MyCellerView().environmentObject(testdata1)
            //ShowDiscription().environmentObject(testdata1)
            //}
        }
    }
}
