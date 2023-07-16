//
//  ContentView.swift
//  HelloWorld
//
//  Created by Mukesh Thamilvanan on 7/7/23.
//

import SwiftUI

struct ContentView: View {
    @State private var oneCent = 0
    
    var body: some View {
        
//        HStack {
//            VStack {
//                Image(systemName: "globe")
//                    .imageScale(.large)
//                    .foregroundColor(.accentColor)
//                Text("Third")
//            }
//        }.padding()
        
        
        
        //adding a few buttons to add
            // text box then increment then total of that number
        //  table with 3 cols
        
        HStack{
            Stepper("One Cent", value: $oneCent, in: 0...100)
            // stepper  - TEXT -- Starting -- MaxValue
            Text("\(oneCent)")
        }
        
        
        
    }
    

    
    
}

struct ContentView_Previews:
    // shows the preview
    PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

struct Previews_ContentView_Previews: PreviewProvider {
    static var previews: some View {
       ContentView()
    }
}
