<?xml version="1.0"?>
<flowgorithm fileversion="2.11">
    <attributes>
        <attribute name="name" value="Moo-Kata Vender"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-15 05:56:21 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7REVTS1RPUC1ORFVLTUZLOzIwMjUtMDctMTU7MTE6MDA6MDAgQU07MTAw"/>
        <attribute name="edited" value="Y29tcHV0ZXI7REVTS1RPUC1ORFVLTUZLOzIwMjUtMDctMTU7MDU6NTY6MjEgUE07NDszMzg2"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="childPrice, adultPrice, numChild, numAdult, total" type="Integer" array="False" size=""/>
            <assign variable="childPrice" expression="120"/>
            <assign variable="adultPrice" expression="189"/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="numChild"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="numAdult"/>
            <assign variable="total" expression="(numChild * childPrice) + (numAdult * adultPrice)"/>
            <output expression="&quot;You ordered &quot; &amp; numChild &amp; &quot; children and &quot; &amp; numAdult &amp; &quot; adults.&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot; &amp; total &amp; &quot; Baht.&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>