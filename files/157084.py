<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="testkong1"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 04:51:45 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDM6MTQ6NDQgUE07MjU3Nw=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6NTE6NDUgUE07MjM7Mjc0MA=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="price, discount, total" type="Real" array="False" size=""/>
            <declare name="child" type="Integer" array="False" size=""/>
            <declare name="adult" type="Integer" array="False" size=""/>
            <assign variable="total" expression="0"/>
            <assign variable="child" expression="0"/>
            <assign variable="adult" expression="0"/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="child"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="adult"/>
            <assign variable="total" expression="(child*120)+(adult*189)"/>
            <output expression="&quot;You ordered &quot; &amp;child&amp; &quot; children and &quot; &amp;adult&amp; &quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price:&quot;&amp;total&amp;&quot;Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>