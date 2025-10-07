<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="work4lab4"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 05:00:59 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6NDk6MjAgUE07MjU4MA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDU6MDA6NTkgUE07MTsyNjg4"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, years, i" type="Real" array="False" size=""/>
            <assign variable="i" expression="1"/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="years"/>
            <while expression="i &lt;= years">
                <assign variable="money" expression="money *(1 + interest/100)"/>
                <output expression="&quot;Year &quot;&amp; i &amp;&quot;:&quot;&amp; money" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>