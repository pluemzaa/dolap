<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab44"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 02:56:30 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6NDQ6MjUgUE07MjU3OA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6NTY6MzAgUE07MzsyNjg3"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="year, per, i, total" type="Integer" array="False" size=""/>
            <declare name="mon" type="Real" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="mon"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="per"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="i" expression="0"/>
            <while expression="i &lt; year">
                <output expression="&quot;Year &quot; &amp; (i+1) &amp; &quot;:&quot;" newline="False"/>
                <assign variable="mon" expression="mon * (1 + (per / 100))"/>
                <output expression="mon" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>