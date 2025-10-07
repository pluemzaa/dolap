<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="worklap4_1"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 02:51:57 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6MDQ6NDMgUE07MjU3NA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6NTE6NTcgUE07NDsyNjky"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="price, total, childprice, adultprice" type="Integer" array="False" size=""/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <assign variable="childPrice" expression="120"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <assign variable="adultPrice" expression="189"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="childPrice"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="adultPrice"/>
            <assign variable="total" expression="(childPrice*120)+(adultPrice*189)"/>
            <output expression="&quot;You ordered &quot;&amp; childPrice &amp; &quot; children and &quot; &amp; adultPrice &amp; &quot; adults &quot;" newline="True"/>
            <output expression="&quot;Total price: &quot; &amp; total &amp; &quot; Baht &quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>