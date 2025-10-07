<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="FClab04"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 05:05:06 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6MzY6MTkgUE07MjU4NA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDU6MDU6MDYgUE07MjsyNjg2"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="in, y, L" type="Integer" array="False" size=""/>
            <declare name="m" type="Real" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="m"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="in"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="y"/>
            <assign variable="L" expression="1"/>
            <while expression="L&lt;=y">
                <assign variable="m" expression="m*(1+in*0.01)"/>
                <output expression="&quot;Year &quot; &amp; L &amp; &quot; : &quot; &amp; m" newline="True"/>
                <assign variable="L" expression="L+1"/>
            </while>
        </body>
    </function>
</flowgorithm>