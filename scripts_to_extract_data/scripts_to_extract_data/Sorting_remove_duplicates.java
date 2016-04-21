/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication30;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.Set;

/**
 *
 * @author aiyerganapathy
 */
public class Sorting_remove_duplicates {

    /**
     * @param args the command line arguments
     */
   
    public static void main(String[] args) throws IOException {
        String fileName = "C:\\Users\\Aiyer\\Desktop\\names2.txt";
        //PrintWriter writer = new PrintWriter(new BufferedWriter(new FileWriter("C:\\Users\\Aiyer\\Desktop\\movie_names1.txt", true)));
        try {
            BufferedReader reader = new BufferedReader(new FileReader(fileName));
    ArrayList<String> lines = new ArrayList<String>(1000000); // maybe should be bigger
    String line;
    while ((line = reader.readLine()) != null) {
        if(!lines.contains(line))
        {lines.add(line);}
    }
    Collections.sort(lines);
    reader.close();
    BufferedWriter writer = new BufferedWriter(new FileWriter("C:\\Users\\Aiyer\\Desktop\\movie_name_final.txt"));
    for (String unique : lines) {
        writer.write(unique);
        writer.newLine();
    }
    writer.close();
        }
        catch (IOException e){
            System.out.println(e);
        }
    }
    
}
