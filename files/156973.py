<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 02:59:42 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6Mjk6MzYgUE07MjU4Mw=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6NTk6NDIgUE07NTsyNjk1"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="in, year, i, n, y" type="Integer" array="False" size=""/>
            <declare name="ins, total, mon" type="Real" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="mon"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="in"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="i" expression="0"/>
            <assign variable="n" expression="0"/>
            <assign variable="total" expression="0"/>
            <while expression="i&lt;year">
                <assign variable="mon" expression="mon*(1+in*0.01)"/>
                <assign variable="i" expression="i+1"/>
                <output expression="&quot;Year &quot;&amp;i&amp;&quot;: &quot;&amp;mon" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>