<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="test4"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 02:48:57 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6Mzg6MzQgUE07MjU4MQ=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6NDg6NTcgUE07MTsyNjk1"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, inte, years, i, total" type="Real" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="inte"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="years"/>
            <assign variable="i" expression="0"/>
            <while expression="i&lt;years">
                <assign variable="total" expression="money*(1+(inte/100))"/>
                <assign variable="money" expression="total"/>
                <output expression="&quot;Year &quot;&amp;(i+1)&amp;&quot;:&quot;&amp; total" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>