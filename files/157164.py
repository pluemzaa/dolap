<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Moo kata"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 06:36:02 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDU6NTc6MzEgUE07MjU4Mg=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDY6MzY6MDIgUE07NDsyNjg5"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="C, A, Z, X" type="Integer" array="False" size=""/>
            <assign variable="C" expression="120"/>
            <assign variable="A" expression="189"/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="z"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="x"/>
            <declare name="total" type="Integer" array="False" size=""/>
            <assign variable="total" expression="(Z*120)+(X*189)"/>
            <output expression="&quot;You ordered &quot;&amp; Z &amp;&quot; children&quot;&amp;&quot; and &quot;&amp; X &amp;&quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price:&quot;&amp; total &amp; &quot;Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>