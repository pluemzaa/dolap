<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_4"/>
        <attribute name="authors" value="TUF GAMING"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-21 09:35:09 PM"/>
        <attribute name="created" value="VFVGIEdBTUlORztBU1VTOzI1NjgtMDctMTE7MTI6NTA6MTEgUE07MjMwNg=="/>
        <attribute name="edited" value="VFVGIEdBTUlORztBU1VTOzI1NjgtMDctMjE7MDk6MzU6MDkgUE07MzsyNDMz"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="year, per, i, total" type="Integer" array="False" size=""/>
            <declare name="mon" type="Real" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="mon"/>
            <output expression="&quot;Input interest(%):&quot;" newline="True"/>
            <input variable="per"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="i" expression="0"/>
            <while expression="i &lt; year">
                <output expression="&quot;Year&quot; &amp; (i+1)&amp; &quot;:&quot;" newline="False"/>
                <assign variable="mon" expression="mon * (1 + (per / 100))"/>
                <output expression="mon" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>