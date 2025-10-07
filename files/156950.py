<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Lab4.4"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 02:47:42 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6MzQ6NTUgUE07MjU4MA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6NDc6NDIgUE07MzsyNjkw"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="i, y, k" type="Integer" array="False" size=""/>
            <declare name="x" type="Real" array="False" size=""/>
            <assign variable="k" expression="1"/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="x"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="y"/>
            <while expression="k &lt;= y">
                <assign variable="x" expression="x*(1+(i*0.01))"/>
                <output expression="&quot;Year &quot;&amp;k&amp;&quot; : &quot;&amp;x" newline="True"/>
                <assign variable="k" expression="k+1"/>
            </while>
        </body>
    </function>
</flowgorithm>